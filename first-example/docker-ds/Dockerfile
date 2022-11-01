FROM eclipse-temurin:8-jre

## install DolphinScheduler
RUN wget https://dlcdn.apache.org/dolphinscheduler/3.1.0/apache-dolphinscheduler-3.1.0-bin.tar.gz; \
  tar -zxvf apache-dolphinscheduler-3.1.0-bin.tar.gz

RUN cp -r apache-dolphinscheduler-3.1.0-bin /opt/dolphinscheduler; \
  rm apache-dolphinscheduler-3.1.0-bin.tar.gz;

RUN rm -r apache-dolphinscheduler-3.1.0-bin 

FROM continuumio/anaconda3 

RUN apt update; \
    apt -y install sudo; \
    apt -y install git; \
    apt -y install vim; \
    rm -rf /var/lib/apt/lists/*

ENV TZ Asia/Shanghai

ENV DOCKER true

RUN python -m pip install mlflow==1.30.0 dvc

ENV JAVA_HOME=/opt/java/openjdk

COPY --from=0 $JAVA_HOME $JAVA_HOME

COPY --from=0 /opt/dolphinscheduler /opt/dolphinscheduler 

WORKDIR /opt/dolphinscheduler/standalone-server

ENV PATH="${JAVA_HOME}/bin:${PATH}"

ADD common.properties /opt/dolphinscheduler/standalone-server/conf/common.properties

RUN echo 'export PATH="/opt/conda/bin:$PATH"' >> /opt/dolphinscheduler/standalone-server/conf/dolphinscheduler_env.sh; 
RUN echo 'export PYTHON_HOME="/opt/conda/bin/python"' >> /opt/dolphinscheduler/standalone-server/conf/dolphinscheduler_env.sh; 

RUN echo "no" | dpkg-reconfigure dash

ADD .condarc /root/.condarc

CMD [ "/bin/bash", "./bin/start.sh" ]
