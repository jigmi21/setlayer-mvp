import os
import pandas as pd

def load_csv_tables(data_dir="data/"):
    """
    Load all CSV files from a directory into a dictionary of DataFrames.
    
    Args:
        data_dir (str): Path to the folder containing CSVs.
    
    Returns:
        dict[str, pd.DataFrame]: Dictionary of table_name -> DataFrame
    """
    tables = {}
    for filename in os.listdir(data_dir):
        if filename.endswith(".csv"):
            path = os.path.join(data_dir, filename)
            table_name = os.path.splitext(filename)[0]
            df = pd.read_csv(path)
            tables[table_name] = df
            
    return tables
