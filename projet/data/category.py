from data.db import DB

class Category:
    def __init__(self) -> None:
        self.db = DB(
                        host = 'localhost', 
                        user = 'root', 
                        passwd = 'hR!9gT+pLq6s', 
                        db = 'gestion_de_stock'
                    )

    def create(self, name):
        query = "INSERT INTO categories (name) VALUES (%s)"
        params = (name,)
        self.db.executeQuery(query, params)

    def read(self):
        query = 'SELECT * FROM categories'
        return self.db.executeQuery(query)
    
    def update(self, id, name):
        query = 'UPDATE categories SET name=%s WHERE id=%s'
        params = (name, id)
        self.db.executeQuery(query, params)
    
    def delete(self, id):
        query = 'DELETE FROM categories WHERE id=%s'
        params = (id,)
        self.db.executeQuery(query, params)
    