import pandas as pd
from src.constants import COUNTRY_CODE_PATH

def clean_basic(df):
    print(" Cleaning data")
    
    df_clean = df.copy()
    
    #tất cả là No nên xóa luôn
    if 'Switch to order menu' in df_clean.columns:
        df_clean = df_clean.drop(columns=['Switch to order menu'])
    
    #Xóa khoảng trắng
    string_cols = df_clean.select_dtypes(include=['object']).columns
    for col in string_cols:
        df_clean[col] = df_clean[col].astype(str).str.strip()
        
    # Xử lí null
    if 'Cuisines' in df_clean.columns:
        df_clean['Cuisines'] = df_clean['Cuisines'].fillna('Others')
        
    # Đọc file country code
    df_country = pd.read_excel(COUNTRY_CODE_PATH)
    df_country['Country'] = df_country['Country'].astype(str).str.strip()
    
    # Thực hiện LEFT JOIN dựa trên cột chung là 'Country Code'
    df_final = pd.merge(df_clean, df_country, on='Country Code', how='left')
    
    print(f"Clean hoàn tất, kích thước dữ liệu hiện tại: {df_final.shape}")
    return df_final
 

