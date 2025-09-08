import sqlite3

class Database:
    def __init__(self, db_name="library.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS processed_data (id INTEGER PRIMARY KEY, column1 TEXT, column2 TEXT)"
        )
        self.conn.commit()

    def insert_data(self, column1, column2):
        self.cursor.execute(
            "INSERT INTO processed_data (column1, column2) VALUES (?, ?)", (column1, column2)
        )
        self.conn.commit()

    def fetch_all_data(self):
        self.cursor.execute("SELECT * FROM processed_data")
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()