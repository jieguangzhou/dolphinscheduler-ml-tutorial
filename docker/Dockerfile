FROM eclipse-temurin:8-jre

ENV DOCKER true

RUN apt update ; \
    apt install -y sudo ; \
    apt install vim; \
    rm -rf /var/lib/apt/lists/*

ENV TZ Asia/Shanghai

## install DolphinScheduler
RUN wget https://dlcdn.apache.org/dolphinscheduler/3.1.0/apache-dolphinscheduler-3.1.0-bin.tar.gz; \
  tar -zxvf apache-dolphinscheduler-3.1.0-bin.tar.gz

RUN cp -r apache-dolphinscheduler-3.1.0-bin /opt/dolphinscheduler; \
  rm apache-dolphinscheduler-3.1.0-bin.tar.gz;

EXPOSE 12345 25333

WORKDIR /opt/dolphinscheduler/standalone-server

COPY --from=continuumio/miniconda3 /opt/conda /opt/conda

RUN echo 'export PATH="/opt/conda/bin:$PATH"' >> conf/dolphinscheduler_env.sh; 

ENV PATH="/opt/conda/bin:$PATH"

RUN python -m pip install mlflow

RUN echo "no" | dpkg-reconfigure dash

RUN apt -y update; \
    apt -y install git

RUN chmod 777 -R /opt/conda

CMD [ "/bin/bash", "./bin/start.sh" ]
