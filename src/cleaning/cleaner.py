import pandas as pd

def profile_table(df: pd.DataFrame) -> dict:
    return {
        "rows": len(df),
        "columns": list(df.columns),
        "nulls_per_column": df.isnull().sum().to_dict(),
        "duplicate_rows": df.duplicated().sum(),
        "data_types": df.dtypes.astype(str).to_dict(),
    }


def clean_table(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Example rules:
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    df = df.drop_duplicates()
    df = df.dropna(axis=1, how="all")  # drop columns with all NaNs
    df = df.dropna(axis=0, how="all")  # drop rows with all NaNs

    return df

def clean_data(tables: dict[str, pd.DataFrame]) -> dict[str, pd.DataFrame]:
    cleaned = {}
    for name, df in tables.items():
        profile = profile_table(df)
        cleaned_df = clean_table(df)
        cleaned[name] = cleaned_df
    return cleaned
