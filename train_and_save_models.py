import pandas as pd
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib # Library to save model objects

print("Starting model training process...")

# --- Reusable Preprocessing Function ---
def _preprocess_data(df):
    processed_df = df.copy()
    processed_df['Target'] = processed_df['Target'].apply(lambda x: 1 if x == 'Dropout' else 0)
    
    label_encoders = {}
    for col in sorted(processed_df.select_dtypes(include=['object']).columns):
        if col != 'Target':
            le = LabelEncoder()
            processed_df[col] = le.fit_transform(processed_df[col].astype(str))
            label_encoders[col] = le
            
    X = processed_df.drop('Target', axis=1)
    y = processed_df['Target']
    model_columns = X.columns.tolist()
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return X_scaled, y, scaler, label_encoders, model_columns

# --- Train and Save 1-Semester Model ---
try:
    print("Training 1-Semester model...")
    df_1sem_raw = pd.read_csv('Data(Nosem).csv')
    df_1sem_raw.rename(columns={'Daytime/evening attendance\t': 'Daytime/evening attendance', 'Student Mail': 'Parent Mail'}, inplace=True)
    
    id_cols = ['Student ID', 'Student Name', 'Parent Mail']
    X_train, y_train, scaler, encoders, model_cols = _preprocess_data(df_1sem_raw.drop(columns=id_cols, errors='ignore'))

    model_1sem = SVC(kernel='rbf', probability=True, class_weight='balanced', random_state=42).fit(X_train, y_train)

    # Save all the necessary objects
    joblib.dump(model_1sem, 'model_1sem.joblib')
    joblib.dump(scaler, 'scaler_1sem.joblib')
    joblib.dump(encoders, 'encoders_1sem.joblib')
    joblib.dump(model_cols, 'model_cols_1sem.joblib')
    
    print("✅ 1-Semester model and assets saved successfully.")
except Exception as e:
    print(f"❌ Error training 1-Semester model: {e}")

# --- Train and Save 2-Semester Model ---
try:
    print("Training 2-Semester model...")
    df_2sem_raw = pd.read_csv('Data(Sem-2).csv')
    df_2sem_raw.rename(columns={'Daytime/evening attendance\t': 'Daytime/evening attendance', 'Student Mail': 'Parent Mail'}, inplace=True)
    
    X_train, y_train, scaler, encoders, model_cols = _preprocess_data(df_2sem_raw.drop(columns=id_cols, errors='ignore'))
    
    model_2sem = SVC(kernel='rbf', probability=True, class_weight='balanced', random_state=42).fit(X_train, y_train)

    # Save all the necessary objects
    joblib.dump(model_2sem, 'model_2sem.joblib')
    joblib.dump(scaler, 'scaler_2sem.joblib')
    joblib.dump(encoders, 'encoders_2sem.joblib')
    joblib.dump(model_cols, 'model_cols_2sem.joblib')

    print("✅ 2-Semester model and assets saved successfully.")
except Exception as e:
    print(f"❌ Error training 2-Semester model: {e}")