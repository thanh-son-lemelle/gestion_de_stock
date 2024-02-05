import mysql.connector
from mysql.connector import errorcode

class DB:
    def __init__(self, host, user, passwd, db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
    
    def connect(self):
        if self.db is not None:
            try:
                self.conn = mysql.connector.connect(
                                                        host=self.host, 
                                                        user=self.user, 
                                                        passwd=self.passwd, 
                                                        db=self.db
                                                    )
                self.cursor = self.conn.cursor()
            except mysql.connector.Error as e:
                print(e)
                if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
                elif e.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                    createDb = input("Do you want to create the database? (y/n): ")
                    if createDb == 'y':
                        self.db = None
                        self.createDb()
                    else:
                        exit()
        elif self.db == None:
            try:
                self.conn = mysql.connector.connect(
                                                        host=self.host, 
                                                        user=self.user, 
                                                        passwd=self.passwd,
                                                        db = 'mysql'
                                                    )
                self.cursor = self.conn.cursor()
            except mysql.connector.Error as e:
                print(e)
                if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
        

    def disconnect(self):
        self.conn.close()

    def executeQuery(self, query, params=None):
        self.connect()
        self.cursor.execute(query, params or ())
        result = self.cursor.fetchall()
        self.conn.commit()
        self.disconnect()
        return result
    
    def createDb(self):
        self.connect()
        self.cursor.execute("CREATE DATABASE gestion_de_stock")
        self.disconnect()
        print("Database created successfully")
        self.db = 'gestion_de_stock'
        self.createTables()
    
    def createTables(self):
        self.connect()
        self.cursor.execute(
            """
            CREATE TABLE categories (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL
            )
            """
        )
        self.cursor.execute(
            """
            CREATE TABLE products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                description VARCHAR(255) NOT NULL,
                price FLOAT NOT NULL,
                quantity INT NOT NULL,
                id_category INT NOT NULL,
                FOREIGN KEY (id_category) REFERENCES categories(id)
            )
            """
        )
        self.disconnect()
        print("Tables created successfully")
