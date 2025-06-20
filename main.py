from src.connectors.csv_connector import load_csv_tables

def main():
    print("🚀 SetLayer MVP Starting...")

    # Step 1: Load data from CSV files
    tables = load_csv_tables("data/")

    # Step 2: Preview loaded tables
    for name, df in tables.items():
        print(f"\n📄 Table: {name.upper()}")
        print(df.head())

    # Placeholder: Later we add cleaning, normalization, modeling
    print("\n✅ Data loading complete. Ready for next steps...")

if __name__ == "__main__":
    main()