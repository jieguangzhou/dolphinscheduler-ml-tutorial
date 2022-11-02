import pandas as pd
import os
from sklearn.model_selection import train_test_split

all_data_path = '/tmp/ds-ml-example/raw'

train_data = pd.read_csv(os.path.join(all_data_path, 'train.csv'))
test_data = pd.read_csv(os.path.join(all_data_path, 'test.csv'))

# select top n rows
# top_n = 300000
top_n = ${top_n}

train_data = train_data.iloc[:top_n, :]

# output_path = "/tmp/ds-ml-example/preprocessed"
output_path = "${output_path}"
os.makedirs(output_path, exist_ok=True)

# Save the data
train_data.to_csv(os.path.join(output_path, 'train.csv'), index=False)

# Separate part of the test set for inference use
test_data, inference_data = train_test_split(test_data, test_size=0.01, random_state=42)
test_data.to_csv(os.path.join(output_path, 'test.csv'), index=False)
inference_data.to_csv(os.path.join(output_path, 'inference.csv'), index=False)
