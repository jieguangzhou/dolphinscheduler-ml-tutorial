import pandas as pd
import os
from sklearn.model_selection import train_test_split

all_data_path = '/data/raw/airplane/all'

train_data = pd.read_csv(os.path.join(all_data_path, 'train.csv'))
test_data = pd.read_csv(os.path.join(all_data_path, 'test.csv'))

# select top n rows
# top_n = 300000
top_n = ${top_n}

train_data = train_data.iloc[:top_n, :]

# Split the data into train
train, dev = train_test_split(train_data, test_size=0.2, random_state=42)


# output_path = "/data/preprocessing/airplane/data"
output_path = "${output_path}"
os.makedirs(output_path, exist_ok=True)

# Save the data
train.to_csv(os.path.join(output_path, 'train.csv'), index=False)
dev.to_csv(os.path.join(output_path, 'dev.csv'), index=False)
test_data.to_csv(os.path.join(output_path, 'test.csv'), index=False)
