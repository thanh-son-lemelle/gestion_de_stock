from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QDialog, QWidget, QSizePolicy, QSplitter
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QAction, QColor
from frontend.dashboard import Dashboard

import sys


# On définit une classe pour notre nouvelle fenêtre.
class MyWindow(QMainWindow):

    # Le constructeur de notre classe de fenêtre.
    def __init__(self, user):
        # On initialise la fenêtre, notamment en rappelant le constructeur parent. 
        super(MyWindow, self).__init__()
        self.user = user
        self.setWindowTitle("Application de gestion de stock")
        self.setWindowIcon(QIcon("icon.png"))

        # On définit la taille de la fenêtre.
        self.resize(800, 600)
        menuBar = self.menuBar()
        Inventory = menuBar.addMenu("&Inventory")
        Inventory.addAction("&Add Product")
        Inventory.addAction("&List Product")
        Inventory.addAction("&Search Product")
        Inventory.addAction("&Delete Product")
        Inventory.addAction("&Update Product")
        
        price = menuBar.addMenu("&Price")
        price.addAction("&Add Price")
        price.addAction("&List Price")
        price.addAction("&Search Price")
        price.addAction("&Delete Price")
        price.addAction("&Update Price")

        quantity = menuBar.addMenu("&Quantity")
        quantity.addAction("&Add Quantity")
        quantity.addAction("&List Quantity")
        quantity.addAction("&Search Quantity")
        quantity.addAction("&Delete Quantity")
        quantity.addAction("&Update Quantity")
        # On crée une barre d'outils.
        toolbar = self.addToolBar("Main toolbar")
        toolbar.setAllowedAreas(Qt.TopToolBarArea | Qt.BottomToolBarArea)
        toolbar.setMovable(False)

        # On y ajoute un premier bouton addproduct.
        addProductAction = QAction(QIcon("add.png"), "Add Product", self)
        addProductAction.setStatusTip("Add Product")
        addProductAction.triggered.connect(self.doSomething)
        toolbar.addAction(addProductAction)

        # On y ajoute un second bouton updateproduct.
        updateProductAction = QAction(QIcon("update.png"), "Update Product", self)
        updateProductAction.setStatusTip("Update Product")
        updateProductAction.triggered.connect(self.doSomething)
        toolbar.addAction(updateProductAction)

        # On y ajoute un troisième bouton deleteproduct.
        deleteProductAction = QAction(QIcon("delete.png"), "Delete Product", self)
        deleteProductAction.setStatusTip("Delete Product")
        deleteProductAction.triggered.connect(self.doSomething)
        toolbar.addAction(deleteProductAction)

        # On crée un widget représentant la zone centrale de la fenêtre.
        self.central_Widget = QWidget()
        self.setCentralWidget(self.central_Widget)

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

        self.addButton = QPushButton("Add Product")
        self.addButton.clicked.connect(self.add_product)

        self.addButtonDelete = QPushButton("Delete Product")
        self.addButtonDelete.clicked.connect(self.delete_product)

        # Ajoutez les boutons à la disposition principale
        self.layout.addWidget(self.addButton)
        self.layout.addWidget(self.addButtonDelete)

        self.central_Widget.setLayout(self.layout)

        # Chargez les produits au démarrage de l'application
        self.load_products_with_category_from_database()
        self.load_products_from_database()
        self.load_categories_from_database()
    
    def doSomething(self):
        print("Doing something")


    def load_products_with_category_from_database(self):
        # Obtenez tous les produits depuis la base de données
        data = self.user.readProductswithCategory()

        # Effacez toutes les lignes actuelles dans la table
        self.product_with_category_table.setRowCount(0)

        # Remplissez la table avec les données des produits
        for row, product in enumerate(data):
            self.product_with_category_table.insertRow(row)
            for col, value in enumerate(product):
                item = QTableWidgetItem(str(value))
                item.setForeground(QColor(158, 178, 177))
                self.product_with_category_table.setItem(row, col, item)

    def load_products_from_database(self):
        # Obtenez tous les produits depuis la base de données
        data = self.user.readProducts()

        # Effacez toutes les lignes actuelles dans la table
        self.product_table.setRowCount(0)

        # Remplissez la table avec les données des produits
        for row, product in enumerate(data):
            self.product_table.insertRow(row)
            for col, value in enumerate(product):
                item = QTableWidgetItem(str(value))
                item.setForeground(QColor(158, 178, 177))
                self.product_table.setItem(row, col, item)

    def load_categories_from_database(self):
        # Obtenez toutes les catégories depuis la base de données
        data = self.user.readCategories()

        # Effacez toutes les lignes actuelles dans la table
        self.category_table.setRowCount(0)

        # Remplissez la table avec les données des catégories
        for row, category in enumerate(data):
            self.category_table.insertRow(row)
            for col, value in enumerate(category):
                item = QTableWidgetItem(str(value))
                item.setForeground(QColor(158, 178, 177))
                self.category_table.setItem(row, col, item)

    def add_product(self):
        dialog = Dashboard(self)
        result = dialog.exec()

        if result == QDialog.Accepted:
            product_data = dialog.get_product_data()

            # Ajoutez le produit à la base de données
            self.user.createProduct(
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
            self.user.deleteProduct(product_id)

            # Chargez à nouveau les produits depuis la base de données et mettez à jour le tableau
            self.load_products_with_category_from_database()




