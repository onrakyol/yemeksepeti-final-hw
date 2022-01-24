import sqlite3 as sql

class CreateDB():    
    def __init__(self, db_file, date_table, *args):
        self.db_file = db_file        
        self.date_table = date_table
        self.con = sql.Connection
        self.cur = sql.Cursor
        self.query_ = ""

    def db_connect(self):
        db_file = self.db_file
        self.con = sql.connect(db_file)

    def db_close (self):
        self.con.close()

    def open_table(self):
        self.query_ = f"""
            CREATE TABLE IF NOT EXISTS datas{self.date_table} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                fullname TEXT NOT NULL,
                emailuserlk INTEGER NOT NULL DEFAULT 1,
                usernamelk INTEGER NOT NULL DEFAULT 1,
                yob INTEGER,
                mob INTEGER,
                dob INTEGER,
                country TEXT NOT NULL,
                ap INTEGER NOT NULL DEFAULT 1
            );
        """
    
    def open_cur(self):
        self.cur = self.con.cursor()
        self.cur.execute(self.query_)
        self.con.commit()
    
    def create_table(self):
        self.db_connect()
        self.open_table()
        self.open_cur()
        self.db_close()
  

    def execute_table(self,table_query):
        self.db_connect()
        self.cur = self.con.cursor()
        self.cur.execute(table_query)
        self.con.commit()
