import pandas as pd
from src.constants import RAW_DATA_PATH
from src.constants import PROCESSED_DATA_PATH

def load_raw_data():
    return pd.read_csv(RAW_DATA_PATH)

def save_processed_data(df):
    df.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f" Đã lưu file sạch tại: {PROCESSED_DATA_PATH}")