import pandas as pd
from src.constants import RAW_DATA_PATH, PROCESSED_DATA_PATH_DA, PROCESSED_DATA_PATH_DS_TEST,PROCESSED_DATA_PATH_DS_TRAIN

def load_raw_data():
    return pd.read_csv(RAW_DATA_PATH, encoding='latin-1')

def save_processed_data_da(df):
    df.to_csv(PROCESSED_DATA_PATH_DA, index=False, encoding='utf-8')
    print(f" Đã lưu file sạch tại: {PROCESSED_DATA_PATH_DA}")

def save_processed_data_ds_train(df):
    df.to_csv(PROCESSED_DATA_PATH_DS_TRAIN, index=False, encoding='utf-8')
    print(f" Đã lưu file sạch tại: {PROCESSED_DATA_PATH_DS_TRAIN}")


def save_processed_data_ds_test(df):
    df.to_csv(PROCESSED_DATA_PATH_DS_TEST, index=False, encoding='utf-8')
    print(f" Đã lưu file sạch tại: {PROCESSED_DATA_PATH_DS_TEST}")
