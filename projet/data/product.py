from data.db import DB

class Product:
    def __init__(self):
        self.db = DB(host = 'localhost', user = 'root', passwd = 'hR!9gT+pLq6s', db = 'gestion_de_stock')
        
    def create(self, name, description, price, quantity, id_category):
        query = 'insert into products (name, description, price, quantity, id_category) values (%s, %s, %s, %s, %s)'
        params = (name, description, price, quantity, id_category)
        self.db.executeQuery(query, params)
        
    def read(self):
        query = 'select * from products'
        return self.db.executeQuery(query)
    
    def update(self, id, name, description, price, quantity, id_category):
        query = 'update products set name=%s, description=%s, price=%s, quantity=%s, id_category=%s where id=%s'
        params = (name, description, price, quantity, id_category, id)
        self.db.executeQuery(query, params)
    
    def delete(self, id):
        query = 'delete from products where id=%s'
        params = (id,)
        self.db.executeQuery(query, params)

    def readProductswithCategory(self):
        query = 'select products.id, products.name, products.description, products.price, products.quantity, categories.name from products inner join categories on products.id_category = categories.id'
        return self.db.executeQuery(query)
    
    #=============================================================
    #================non used methods (yet)=======================
    #=============================================================
    def readByCategory(self, id_category):
        query = 'select * from products where id_category=%s'
        params = (id_category,)
        return self.db.executeQuery(query, params)
    
    def readById(self, id):
        query = 'select * from products where id=%s'
        params = (id,)
        return self.db.executeQuery(query, params)
    
    def updateQuantity(self, id, quantity):
        query = 'update products set quantity=%s where id=%s'
        params = (quantity, id)
        self.db.executeQuery(query, params)
    
    def updateQuantityByCategory(self, id_category, quantity):
        query = 'update products set quantity=%s where id_category=%s'
        params = (quantity, id_category)
        self.db.executeQuery(query, params)
    
