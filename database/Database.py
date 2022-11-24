import sqlite3

class Database:
    connection = None
    cursor = None

    def __init__(self):
        #global conexao, cursor
        self.conexao = sqlite3.connect("database/imdb.db")
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.commit()
