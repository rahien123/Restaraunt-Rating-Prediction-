import pandas as pd
from src.constants import RAW_DATA_PATH
from src.constants import PROCESSED_DATA_PATH_DA
from src.constants import PROCESSED_DATA_PATH_DS

def load_raw_data():
    return pd.read_csv(RAW_DATA_PATH)

def save_processed_data_da(df):
    df.to_csv(PROCESSED_DATA_PATH_DA, index=False)
    print(f" Đã lưu file sạch tại: {PROCESSED_DATA_PATH_DA}")

def save_processed_data_ds(df):
    df.to_csv(PROCESSED_DATA_PATH_DS, index=False)
    print(f" Đã lưu file sạch tại: {PROCESSED_DATA_PATH_DS}")
