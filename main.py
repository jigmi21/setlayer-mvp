from src.user_interface import DataFrameViewer, QApplication
import sys
from src.connectors.csv_connector import load_csv_tables
from src.cleaning.cleaner import clean_data



def main():
    # Load and clean data
    tables = load_csv_tables("data/")
    cleaned_tables = clean_data(tables)


    df = cleaned_tables["synthetic_loan_data"]

    # Start the PyQt5 app
    app = QApplication(sys.argv)
    viewer = DataFrameViewer(df, title = "synthetic_loan_data")
    viewer.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
