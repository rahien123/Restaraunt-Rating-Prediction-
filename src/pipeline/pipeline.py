from src.data.load_data import load_raw_data, save_processed_data_da, save_processed_data_ds_train,save_processed_data_ds_test
from src.features.build_features import get_da_data, get_ds_data

def run_da_pipeline():
    print("\nSTART DA PIPELINE")
    df = load_raw_data()
    df_da = get_da_data(df)

    save_processed_data_da(df_da)
    print("Hoàn tất DA Pipeline")

def run_ds_pipeline():
    print("\nSTART DS PIPELINE")
    df = load_raw_data()
    df_train, df_test = get_ds_data(df)
    
    save_processed_data_ds_train(df_train)
    save_processed_data_ds_test(df_test)
    
    print("Hoàn tất DS Pipeline")