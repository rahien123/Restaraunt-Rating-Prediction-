from xgboost import XGBClassifier, XGBRegressor
from sklearn.metrics import mean_absolute_error, r2_score, accuracy_score, classification_report
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold, KFold
from sklearn.metrics import (
    accuracy_score, f1_score, classification_report,
    confusion_matrix, ConfusionMatrixDisplay,
    mean_absolute_error, mean_squared_error, r2_score
)


def check_overfitting(model, X_train, y_train, X_valid, y_valid, task='regression'):
    y_train_pred = model.predict(X_train)
    y_valid_pred = model.predict(X_valid)
    
    print(f"Kiểm tra Overfitting cho mô hình: {task}")
    
    if task == 'regression':
        train_mae = mean_absolute_error(y_train, y_train_pred)
        test_mae = mean_absolute_error(y_valid, y_valid_pred)
        train_r2 = r2_score(y_train, y_train_pred)
        test_r2 = r2_score(y_valid, y_valid_pred)
        
        print(f"MAE  - Train: {train_mae:.4f}, Valid: {test_mae:.4f}")
        print(f"R²   - Train: {train_r2:.4f}, Valid: {test_r2:.4f}")
        
        if train_r2 > test_r2 + 0.15: # Nếu R2 train cao hơn test quá 15%
            print("CẢNH BÁO: Mô hình có dấu hiệu Overfitting (Train tốt hơn Valid quá nhiều)!")
        else:
            print("Mô hình ổn định (Gap giữa Train và Valid nhỏ).")
            
    elif task == "classification": 
        train_acc = accuracy_score(y_train, y_train_pred)
        test_acc = accuracy_score(y_valid, y_valid_pred)
        print(f"Accuracy - Train: {train_acc:.4f}, Valid: {test_acc:.4f}")
        
        if train_acc > test_acc + 0.1:
            print("CẢNH BÁO: Mô hình có dấu hiệu Overfitting!")
        else:
            print("Mô hình ổn định")