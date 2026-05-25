import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

COUNTRY_CODE_PATH = os.path.join(BASE_DIR, "data", "raw", "Country-Code.xlsx")
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "zomato.csv")

PROCESSED_DATA_PATH_DA = os.path.join(BASE_DIR, "data", "processed", "clean_da_data.csv")
PROCESSED_DATA_PATH_DS_TRAIN = os.path.join(BASE_DIR, "data", "processed", "clean_ds_train_data.csv")
PROCESSED_DATA_PATH_DS_TEST = os.path.join(BASE_DIR, "data", "processed", "clean_ds_test_data.csv")
