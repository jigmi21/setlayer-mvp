from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtWidgets import QTableView
import sys
from src.connectors.csv_connector import load_csv_tables
from src.cleaning.cleaner import clean_data
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QLabel, QHBoxLayout, QTextEdit)

class PandasModel(QAbstractTableModel):
    def __init__(self, df):
        super().__init__()
        self._df = df

    def rowCount(self, parent=None):
        return len(self._df)

    def columnCount(self, parent=None):
        return len(self._df.columns)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            value = self._df.iloc[index.row(), index.column()]
            return str(value)
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._df.columns[section])
            else:
                return str(self._df.index[section])
        return None

class DataFrameViewer(QWidget):
    def __init__(self, dataframe, title = "data"):
        super().__init__()
        self.setWindowTitle("Setlayer")
        self.setGeometry(100, 100, 1000, 600)  # Wider for side-by-side

        main_layout = QHBoxLayout()  # Horizontal layout to split screen

        # ===== Left Side: Table =====
        table_layout = QVBoxLayout()
        table_label = QLabel(title)
        table_layout.addWidget(table_label)

        model = PandasModel(dataframe)
        table = QTableView()
        table.setModel(model)
        table.resizeColumnsToContents()

        table_layout.addWidget(table)

        # Create a QWidget for the left pane
        table_widget = QWidget()
        table_widget.setLayout(table_layout)

        # ===== Right Side: Summary =====
        summary_layout = QVBoxLayout()
        summary_label = QLabel("Summary:")
        summary_text = QTextEdit()
        summary_text.setReadOnly(True)

        summary_content = str(dataframe.describe(include='all').transpose())
        summary_text.setText(summary_content)

        summary_layout.addWidget(summary_label)
        summary_layout.addWidget(summary_text)

        summary_widget = QWidget()
        summary_widget.setLayout(summary_layout)

        # ===== Combine both widgets =====
        main_layout.addWidget(table_widget, 1)
        main_layout.addWidget(summary_widget, 1)

        self.setLayout(main_layout)