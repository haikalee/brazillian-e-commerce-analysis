import pandas as pd


def to_datetime(df, columns):
    for column in columns:
        df[column] = pd.to_datetime(df[column])
    return df
