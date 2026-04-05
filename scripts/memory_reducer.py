import pandas as pd
import numpy as np

def memory_reducer(path):
    df = pd.read_csv(path)

    for col in df.columns:
        if df[col].dtype == object:
            try:
                df[col] = pd.to_datetime(df[col])
            except (ValueError, TypeError):
                pass

    for col in df.columns:
        col_type = df[col].dtype
        
        if not np.issubdtype(col_type, np.number): ##checks if the column is numeric at all
            continue
        
        col_min = df[col].min()
        col_max = df[col].max()
        
        if np.issubdtype(col_type, np.integer):
            if col_min >= np.iinfo(np.int8).min and col_max <= np.iinfo(np.int8).max:
                df[col] = df[col].astype(np.int8)
            elif col_min >= np.iinfo(np.int16).min and col_max <= np.iinfo(np.int16).max:
                df[col] = df[col].astype(np.int16)
            elif col_min >= np.iinfo(np.int32).min and col_max <= np.iinfo(np.int32).max:
                df[col] = df[col].astype(np.int32)
        else:
            df[col] = df[col].astype(np.float32)
    
    return df