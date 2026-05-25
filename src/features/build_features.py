import pandas as pd
import numpy as np

from src.data.clean_data import clean_basic

def get_da_data(df_in):
    print("\n--- DA Feature Engineering ")
    # 1. Làm sạch thô dữ liệu dùng chung
    df = clean_basic(df_in)
    df_da = df.copy()
    
    # 2.Drop những cột thuần định danh hệ thống hoặc thừa thãi thông tin
    cols_to_drop_da = ['Restaurant ID', 'Country Code', 'Locality Verbose']
    df_da = df_da.drop(columns=[col for col in cols_to_drop_da if col in df_da.columns], errors='ignore')
    
    print(f"-> Hoàn tất xử lí dữ liệu DA. Kích thước: {df_da.shape}")
    return df_da

def get_ds_data(df_in):
    print("\n--- DS Feature Engineering ")
    
    df_ds = clean_basic(df_in) 
    
    # 1. Tạo nhãn số tạm thời
    if 'Rating text' in df_ds.columns:
        rating_mapping = {'Not rated': -1, 'Poor': 0, 'Average': 1, 'Good': 2, 'Very Good': 3, 'Excellent': 4}
        df_ds['rating_numeric_encoded'] = df_ds['Rating text'].map(rating_mapping)
    else:
        df_ds['rating_numeric_encoded'] = -1
        
    # 2. Xóa các cột rác và cột gây rò rỉ dữ liệu
    cols_to_drop_ds = [
        'Restaurant ID', 'Restaurant Name', 'Address', 'Locality', 
        'Locality Verbose', 'Rating color', 'Rating text', 'Country Code'
    ]
    df_ds = df_ds.drop(columns=[col for col in cols_to_drop_ds if col in df_ds.columns], errors='ignore')
    
    # 3. BINARY ENCODING 
    binary_cols = ['Has Table booking', 'Has Online delivery', 'Is delivering now']
    for col in binary_cols:
        if col in df_ds.columns and df_ds[col].dtype == 'object':
            df_ds[col] = df_ds[col].map({'Yes': 1, 'No': 0}).fillna(0).astype(int)
            
    # 4. ONE-HOT ENCODING
    categorical_cols = ['Country Name', 'Currency']
    categorical_cols = [col for col in categorical_cols if col in df_ds.columns]
    if categorical_cols:
        df_ds = pd.get_dummies(df_ds, columns=categorical_cols, drop_first=True, dtype=int)
        
    # 5. FREQUENCY ENCODING
    for col in ['City', 'Cuisines']:
        if col in df_ds.columns:
            freq = df_ds[col].value_counts() / len(df_ds)
            df_ds[col] = df_ds[col].map(freq)
            
    # 6. TÁCH TRAIN / TEST BẰNG BÚT ĐÁNH DẤU TẠM THỜI
    df_train = df_ds[df_ds['rating_numeric_encoded'] != -1].copy()
    df_test = df_ds[df_ds['rating_numeric_encoded'] == -1].copy()
    
    # 7. XÓA BỎ BÚT ĐÁNH DẤU - Tránh lỗi Data Leakage, trả lại ma trận số thuần khiết cho DS
    df_train = df_train.drop(columns=['rating_numeric_encoded'], errors='ignore')
    df_test = df_test.drop(columns=['rating_numeric_encoded'], errors='ignore')
    
    print(f"-> Hoàn tất xử lí dữ liệu DS. Train: {df_train.shape[0]} dòng | Test: {df_test.shape[0]} dòng")
    return df_train, df_test