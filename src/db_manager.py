import pandas as pd
import sqlite3

class DatabaseManager:
    def __init__(self, db_path):

        self.conn = sqlite3.connect(db_path)

    def read_data(self, query):

        return pd.read_sql_query(query, self.conn)

    def close_conn(self):

        self.conn.close()
