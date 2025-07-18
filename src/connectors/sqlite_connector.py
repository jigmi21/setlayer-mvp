
import pandas as pd
from sqlalchemy import create_engine

def load_sqlite_tables(db_path, table_names):
    engine = create_engine(f"sqlite:///{db_path}")
    tables = {}
    for table in table_names:
        df = pd.read_sql_table(table, engine)
        tables[table] = df
    return tables