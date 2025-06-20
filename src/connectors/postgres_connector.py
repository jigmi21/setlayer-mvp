from sqlalchemy import create_engine
import pandas as pd

def load_postgres_tables(uri, table_names):
    """
    Connects to a Postgres DB and loads specified tables into pandas DataFrames.

    Args:
        uri (str): PostgreSQL connection URI
        table_names (list[str]): List of table names to load

    Returns:
        dict[str, pd.DataFrame]: Dictionary of table_name -> DataFrame
    """
    engine = create_engine(uri)
    tables = {}

    for table in table_names:
        print(f"📡 Loading table '{table}'...")
        try:
            df = pd.read_sql_table(table, engine)
            tables[table] = df
            print(f"✅ Loaded '{table}' with shape {df.shape}")
        except Exception as e:
            print(f"❌ Failed to load '{table}': {e}")
    
    return tables