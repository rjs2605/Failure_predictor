import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df: pd.DataFrame):
    df = df.drop(
        columns=[
            "UDI",
            "Product ID",
            "TWF",
            "HDF",
            "PWF",
            "OSF",
            "RNF",
        ]
    )
    
    encoder = LabelEncoder()
    df["Type"] = encoder.fit_transform(df["Type"])

    X = df.drop("Machine failure", axis=1)
    y = df["Machine failure"]

    return X, y, encoder
