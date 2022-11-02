import pandas as pd
import requests
import time

df = pd.read_csv('/tmp/ds-ml-example/raw/test.csv')

df = df.drop(columns=['label'])

df = df.iloc[:8, :]

data = df.to_json(orient='split')

while True:
    try:
        response = requests.get('http://localhost:${port}/health', json=data)
        print(response.content)
        break
    except Exception as e:
        print("wait...")

    time.sleep(1)

response = requests.post(
    url="http://127.0.0.1:${port}/invocations", data=data,
    headers={"Content-type": "application/json"})

print(response.json())
