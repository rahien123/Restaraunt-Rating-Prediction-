from src.data.load_data import load_raw_data, save_processed_data_da, save_processed_data_ds
from src.features.build_features import get_da_data, get_ds_data

def run_da_pipeline():
    df = load_raw_data()
    df_da = get_da_data(df)
    save_processed_data_da(df_da)
    print("Hoàn tất DA Pipeline")

def run_ds_pipeline():
    df = load_raw_data()
    df_ds = get_ds_data(df)
    save_processed_data_ds(df_ds)
    print("Hoàn tất DS Pipeline")