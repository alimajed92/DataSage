import pandas as pd


def transform_csv_to_pandas(filename: str) -> pd.DataFrame:

    df = pd.read_csv(filename)

    return df
