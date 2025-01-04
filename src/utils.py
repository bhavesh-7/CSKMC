import pandas as pd

def save_results(df, file_path):
    df.to_csv(file_path, index=False)
