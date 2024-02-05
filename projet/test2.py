# app/frontend/dashboard.py

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QSplitter, QPushButton, QTableWidget, QTableWidgetItem, QDialog, QFormLayout, QLabel, QLineEdit, QWidget, QSizePolicy, QStyleFactory
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor
from dashboard import Dashboard
from backend.user import User
import sys


class StockManagementApp(QMainWindow):
    
    def __init__(self, data_manager):
        super(StockManagementApp, self).__init__()

        self.data_manager = data_manager

        self.setWindowTitle("Gestion des Stocks")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Utilisez QVBoxLayout comme disposition principale
        self.layout = QVBoxLayout()

        # Créez une boîte de mise en page pour la table
        self.layoutUpper = QVBoxLayout()
        self.layoutLower = QVBoxLayout()
        self.layoutHorizontal = QHBoxLayout()
        self.splitter = QSplitter()
    

        # Créez une table pour afficher les produits
        self.product_table = QTableWidget()
        self.product_table.setColumnCount(6)
        self.product_table.setHorizontalHeaderLabels(['ID', 'Nom', 'Description', 'Prix', 'Quantité', 'ID Catégorie'])

        # Ajustez la politique de taille pour que la table s'étire horizontalement
        self.product_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        

        # Ajoutez la table à la boîte de mise en page de la table
        self.splitter.addWidget(self.product_table)

        # Ajoutez la boîte de mise en page de la table à la disposition principale
        self.layout.addLayout(self.layoutUpper)

        # Créez une table pour afficher les catégories
        self.category_table = QTableWidget()
        self.category_table.setColumnCount(2)
        self.category_table.setHorizontalHeaderLabels(['ID', 'Nom'])

        # Ajustez la politique de taille pour que la table s'étire horizontalement
        self.category_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Ajoutez la table à la boîte de mise en page de la table
        self.splitter.addWidget(self.category_table)

        # Ajoutez la boîte de mise en page de la table à la disposition principale
        self.layoutUpper.addWidget(self.splitter)
        self.layout.addLayout(self.layoutUpper)


        # Créez une table pour afficher les produits avec catégorie
        self.product_with_category_table = QTableWidget()
        self.product_with_category_table.setColumnCount(6)
        self.product_with_category_table.setHorizontalHeaderLabels(['ID', 'Nom', 'Description', 'Prix', 'Quantité', 'Catégorie'])

        # Ajustez la politique de taille pour que la table s'étire horizontalement
        self.product_with_category_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Ajoutez la table à la boîte de mise en page de la table
        self.layoutLower.addWidget(self.product_with_category_table)

        # Ajoutez la boîte de mise en page de la table à la disposition principale
        self.layout.addLayout(self.layoutLower)

        self.addButton = QPushButton("Ajouter Produit")
        self.addButton.clicked.connect(self.add_product)

        self.addButtonDelete = QPushButton("Supprimer Produit")
        self.addButtonDelete.clicked.connect(self.delete_product)

        # Ajoutez les boutons à la disposition principale
        self.layout.addWidget(self.addButton)
        self.layout.addWidget(self.addButtonDelete)

        self.central_widget.setLayout(self.layout)

        # Chargez les produits au démarrage de l'application
        self.load_products_with_category_from_database()
        self.load_products_from_database()
        self.load_categories_from_database()

    def load_products_with_category_from_database(self):
        # Obtenez tous les produits depuis la base de données
        data = self.data_manager.readProductswithCategory()

        # Effacez toutes les lignes actuelles dans la table
        self.product_with_category_table.setRowCount(0)

        # Remplissez la table avec les données des produits
        for row, product in enumerate(data):
            self.product_with_category_table.insertRow(row)
            for col, value in enumerate(product):
                item = QTableWidgetItem(str(value))
                item.setForeground(QColor(255, 255, 255))
                self.product_with_category_table.setItem(row, col, item)

    def load_products_from_database(self):
        # Obtenez tous les produits depuis la base de données
        data = self.data_manager.readProducts()

        # Effacez toutes les lignes actuelles dans la table
        self.product_table.setRowCount(0)

        # Remplissez la table avec les données des produits
        for row, product in enumerate(data):
            self.product_table.insertRow(row)
            for col, value in enumerate(product):
                item = QTableWidgetItem(str(value))
                item.setForeground(QColor(255, 255, 255))
                self.product_table.setItem(row, col, item)

    def load_categories_from_database(self):
        # Obtenez toutes les catégories depuis la base de données
        data = self.data_manager.readCategories()

        # Effacez toutes les lignes actuelles dans la table
        self.category_table.setRowCount(0)

        # Remplissez la table avec les données des catégories
        for row, category in enumerate(data):
            self.category_table.insertRow(row)
            for col, value in enumerate(category):
                item = QTableWidgetItem(str(value))
                item.setForeground(QColor(255, 255, 255))
                self.category_table.setItem(row, col, item)

    def add_product(self):
        dialog = Dashboard(self)
        result = dialog.exec()

        if result == QDialog.Accepted:
            product_data = dialog.get_product_data()

            # Ajoutez le produit à la base de données
            self.data_manager.createProduct(
                product_data['name'],
                product_data['description'],
                product_data['price'],
                product_data['quantity'],
                product_data['id_category']
            )

            # Chargez à nouveau les produits depuis la base de données et mettez à jour le tableau
            self.load_products_with_category_from_database()

    def delete_product(self):
        # Récupérez la ligne sélectionnée
        selected_row = self.product_with_category_table.currentRow()
        
        # Assurez-vous qu'une ligne est sélectionnée
        if selected_row >= 0:
            # Obtenez l'ID du produit à supprimer depuis la colonne ID (colonne 0)
            product_id = int(self.product_with_category_table.item(selected_row, 0).text())

            # Utilisez la classe Backend pour supprimer le produit de la base de données
            self.data_manager.deleteProduct(product_id)

            # Chargez à nouveau les produits depuis la base de données et mettez à jour le tableau
            self.load_products_with_category_from_database()

app = QApplication(sys.argv)
    # Créez une instance de Backend
app.setStyle(QStyleFactory.create('Fusion'))

palette = QPalette()
palette.setColor(QPalette.Window, QColor(53, 53, 53))
palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
palette.setColor(QPalette.Base, QColor(25, 25, 25))
palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
palette.setColor(QPalette.Button, QColor(53, 53, 53))
palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
palette.setColor(QPalette.Highlight, QColor(142, 45, 197))
palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
app.setPalette(palette)


data_manager = User()

    # Passez l'instance de Backend lors de la création de StockManagementApp
window = StockManagementApp(data_manager)

window.setGeometry(100, 100, 800, 700)
window.show()
sys.exit(app.exec())