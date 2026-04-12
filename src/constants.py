import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "Impact_of_Remote_Work_on_Mental_Health.csv")
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "clean_data.csv")
