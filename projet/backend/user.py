from data.category import Category
from data.product import Product
from data.db import DB


class User:
    def __init__(self):

        self.category = Category()
        self.product = Product()
    

    def createCategory(self, name):
        self.category.create(name)
    
    def readCategories(self):
        return self.category.read()
    
    def updateCategory(self, id, name):
        self.category.update(id, name)
    
    def deleteCategory(self, id):
        self.category.delete(id)
    
    def createProduct(self, name, description, price, quantity, id_category):
        self.product.create(name, description, price, quantity, id_category)
    
    def readProducts(self):
        return self.product.read()
    
    def updateProduct(self, id, name, description, price, quantity, id_category):
        self.product.update(id, name, description, price, quantity, id_category)
    
    def deleteProduct(self, id):
        self.product.delete(id)

    def readProductswithCategory(self):
        return self.product.readProductswithCategory()
    
user = User()