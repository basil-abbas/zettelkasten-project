import sqlite3

class Databasemanager():
    def __init__(self, db_name="zettlekastken.db") -> None: 
        self.db_name = db_name
        self.init_db()

    def get_connection(self): #connects the sqlite3 database to the database class
        return sqlite3.connect(self.db_name)
    