import pandas as pd

def clean_basic(df):
    df_clean = df.copy() 
    
    df_clean['Mental_Health_Status'] = df_clean['Mental_Health_Status'].fillna('None')
    df_clean['Physical_Health_Issues'] = df_clean['Physical_Health_Issues'].fillna('None')

    cat_cols = [
        'Gender', 
        'Region', 
        'Industry', 
        'Work_Arrangement', 
        'Mental_Health_Status', 
        'Burnout_Level', 
        'Job_Role'     
    ]
    
    for col in cat_cols:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].astype('category')
            
    return df_clean
 

