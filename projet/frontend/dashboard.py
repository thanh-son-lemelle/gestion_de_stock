# app/frontend/dashboard.py

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QDialog, QFormLayout, QLabel, QLineEdit, QWidget, QSizePolicy
from backend.user import User

class Dashboard(QDialog):
    
    def __init__(self, parent=None):
        super(Dashboard, self).__init__(parent)
        self.setWindowTitle("Ajouter un produit")

        self.name_label = QLabel("Nom:")
        self.name_edit = QLineEdit()

        self.description_label = QLabel("Description:")
        self.description_edit = QLineEdit()

        self.price_label = QLabel("Prix:")
        self.price_edit = QLineEdit()

        self.quantity_label = QLabel("Quantité:")
        self.quantity_edit = QLineEdit()

        self.category_label = QLabel("Catégorie:")
        self.category_edit = QLineEdit()

        self.addButton = QPushButton("Add Product")
        self.addButton.clicked.connect(self.accept)

        layout = QFormLayout()
        layout.addRow(self.name_label, self.name_edit)
        layout.addRow(self.description_label, self.description_edit)
        layout.addRow(self.price_label, self.price_edit)
        layout.addRow(self.quantity_label, self.quantity_edit)
        layout.addRow(self.category_label, self.category_edit)
        layout.addRow(self.addButton)

        self.setLayout(layout)

    def get_product_data(self):
        return {
            'name': self.name_edit.text(),
            'description': self.description_edit.text(),
            'price': float(self.price_edit.text()),
            'quantity': int(self.quantity_edit.text()),
            'id_category': self.category_edit.text()
        }