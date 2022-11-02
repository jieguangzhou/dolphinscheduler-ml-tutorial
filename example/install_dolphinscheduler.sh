
## install DolphinScheduler
wget https://dlcdn.apache.org/dolphinscheduler/3.1.0/apache-dolphinscheduler-3.1.0-bin.tar.gz
tar -zxvf apache-dolphinscheduler-3.1.0-bin.tar.gz
rm apache-dolphinscheduler-3.1.0-bin.tar.gz;

## copy config to dolphinscheduler
cp common.properties apache-dolphinscheduler-3.1.0-bin/standalone-server/conf
echo "export PATH=$(which conda)/bin:\$PATH" >> apache-dolphinscheduler-3.1.0-bin/bin/env/dolphinscheduler_env.sh
echo "export PYTHON_HOME=$(dirname $(which conda))/python" >> apache-dolphinscheduler-3.1.0-bin/bin/env/dolphinscheduler_env.sh

## start DolphinScheduler
cd apache-dolphinscheduler-3.1.0-bin
bash bin/dolphinscheduler-daemon.sh start standalone-server
tail -500f standalone-server/logs/dolphinscheduler-standalone.log


## 安装mlflow，并启动
docker build . -t ds-conda:3.1.0
docker run --name mlflow -p 5000:5000 -d mlflow:1.30.0
