import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_preprocess(file_path):
    df = pd.read_csv(file_path)
    features = df[['Annual Income (k$)', 'Spending Score (1-100)']]
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    return df, scaled_features
