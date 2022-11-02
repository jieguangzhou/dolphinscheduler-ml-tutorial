import os
from flaml.data import load_openml_dataset
import pandas as pd

X_train, X_test, y_train, y_test = load_openml_dataset(
    dataset_id=1169, data_dir='./')

train_data = pd.concat([X_train, y_train], axis=1).reset_index(drop=True)
test_data = pd.concat([X_test, y_test], axis=1).reset_index(drop=True)


train_data['label'] = train_data.pop("Delay")
test_data['label'] = test_data.pop("Delay")


ouput_data = '/data/all'
os.makedirs(ouput_data, exist_ok=True)

train_path = os.path.join(ouput_data, 'train.csv')
test_path = os.path.join(ouput_data, 'test.csv')

train_data.to_csv(train_path, index=False)
test_data.to_csv(test_path, index=False)
