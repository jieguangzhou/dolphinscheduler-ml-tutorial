FROM python:3.10.6-slim-bullseye
RUN pip install --no-cache mlflow==1.30.0

CMD ["/bin/bash", "-c", "mlflow server -h 0.0.0.0 -p 5000 --serve-artifacts --backend-store-uri sqlite:///mlflow.db"]
