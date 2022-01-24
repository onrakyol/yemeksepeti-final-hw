import json
from db_create import CreateDB
from collections import Counter

class Users:    
    def __init__(self,json_file,db_file,date_table):
        self.json_file = json_file
        self.db_file = db_file
        self.jsonData = {}
        self.query = ""
        self.date_table = date_table
        self.dbOp = CreateDB(self.db_file,date_table)
    
    def parse_json(self):
        json_file = open(self.json_file)
        self.jsonData = json.load(json_file)
    
    def insert_data(self):
        for user in self.jsonData:
            self.query = f"""
                INSERT INTO datas{self.date_table}
                    ("email",
                    "fullname",
                    "emailuserlk",
                    "usernamelk",
                    "yob",
                    "mob",
                    "dob",
                    "country",
                    "ap")
                VALUES
                    ("{user["email"]}",
                    "{user["profile"]["name"]}",
                    {1 if sum((Counter(user["email"])&Counter(user["username"])).values()) >= 3 else 0},
                    {1 if user["username"] in user["profile"]["name"].split() else 0},
                    {int(user["profile"]["dob"].split("-")[0])},
                    {int(user["profile"]["dob"].split("-")[1].strip("0"))},
                    {int(user["profile"]["dob"].split("-")[2].strip("0"))},
                    "{user["profile"]["address"].split(", ")[2]}",
                    1);
                """
            self.dbOp.execute_table(self.query)
        self.dbOp.db_close()
    
    def insert_user(self):
        self.parse_json()
        self.insert_data()
