import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "post_pandemic_remote_work_health_impact_2025.csv")
PROCESSED_DATA_PATH_DA = os.path.join(BASE_DIR, "data", "processed", "clean_da_data.csv")
PROCESSED_DATA_PATH_DS = os.path.join(BASE_DIR, "data", "processed", "clean_ds_data.csv")
