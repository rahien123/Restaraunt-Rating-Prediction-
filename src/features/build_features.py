import pandas as pd
import re

from src.data.clean_data import clean_basic

def extract_salary_midpoint(s):
    nums = re.findall(r'\d+', str(s).replace('$', '').replace('K', ''))
    if len(nums) == 2: return (int(nums[0]) + int(nums[1])) * 500
    return 130000 if '120' in str(s) else 0

def process_physical_issues(df):
    temp = df['Physical_Health_Issues'].str.split('; ')
    #đếm physical issuse
    count = temp.apply(lambda x: len([i for i in x if i != 'None']))
    
    dummies = pd.get_dummies(temp.apply(pd.Series).stack()).groupby(level=0).sum()
    if 'None' in dummies.columns:
        dummies = dummies.drop(columns=['None'])
    dummies.columns = [f'has_{col}' for col in dummies.columns]
    
    return dummies, count

#group 24 nhóm về còn n + other nhóm
def group_job_role(df, top_n=10):
    top_jobs = df['Job_Role'].value_counts().nlargest(top_n).index
    return df['Job_Role'].apply(lambda x: x if x in top_jobs else 'Other')

def get_da_data(df_in):
    df = clean_basic(df_in)
    #thêm các cột boolean cho physical health issuse
    phys_dummies, phys_count = process_physical_issues(df)
    df = pd.concat([df, phys_dummies], axis=1)

    #đếm số bệnh physical
    df['Physical_Issues_Count'] = phys_count

    #lương trung bình
    df['Salary_Midpoint'] = df['Salary_Range'].apply(extract_salary_midpoint)

    # 1: Low, 2: Med, 3: High
    df['Burnout_Level'] = df['Burnout_Level'].cat.reorder_categories(['Low', 'Medium', 'High'], ordered=True)
    
    # Gom nhóm Job Role
    df['Job_Role_Grouped'] = group_job_role(df)
    
    drop_cols = ['Survey_Date', 'Physical_Health_Issues', 'Job_Role']
    return df.drop(columns=drop_cols)

def get_ds_data(df_in):
    df = clean_basic(df_in)

    # DS không cần Count (tránh đa cộng tuyến)
    phys_dummies, _ = process_physical_issues(df) 
    df = pd.concat([df, phys_dummies], axis=1)

    df['Salary_Midpoint'] = df['Salary_Range'].apply(extract_salary_midpoint)
    df['Burnout_Level'] = df['Burnout_Level'].cat.reorder_categories(['Low', 'Medium', 'High'], ordered=True)

    #group job rồi mới encode
    df['Job_Role'] = group_job_role(df)
    cat_cols = ['Gender', 'Region', 'Industry', 'Job_Role', 'Work_Arrangement', 'Mental_Health_Status']
    df = pd.get_dummies(df, columns=cat_cols, drop_first=True, dtype=int)
    
    drop_cols = ['Survey_Date', 'Salary_Range', 'Physical_Health_Issues', 'Burnout_Level','Mental_Health_Status_Burnout']
    return df.drop(columns=[c for c in drop_cols if c in df.columns]).select_dtypes(include=['number'])