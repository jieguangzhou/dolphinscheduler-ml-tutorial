from sklearn.metrics import classification_report
import pandas as pd
import json

# data_path = "/home/lucky/WhaleOps/docker-data/train/airplane"
data_path = "${data_path}"

inference_path = f"{data_path}/inference.csv"
df = pd.read_csv(inference_path)

inference_out = f"{data_path}/out.json"
predict_df = pd.DataFrame(json.load(open(inference_out, 'r'))['results'])

print(df)
print(predict_df)

y_true = df['label']
y_pred = predict_df['label']


result: dict = classification_report(y_true, y_pred, output_dict=True)
metrics = result["weighted avg"]
metrics["accuracy"] = result["accuracy"]

print("metrics")
print(metrics)
print()



print("Label distribution: ")
print("y_true", y_true[y_true == 0].count(), y_true[y_true ==
      1].count(), y_true[y_true == 0].count() / y_true.count())
print("y_pred", y_pred[y_pred == 0].count(), y_pred[y_pred ==
      1].count(), y_pred[y_pred == 0].count() / y_pred.count())
