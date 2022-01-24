from db_create import CreateDB
from user import Users
from datetime import datetime
import argparse

parser = argparse.ArgumentParser() 
parser.add_argument("--json_file", "--file", type=str, required=True)
parser.add_argument("--db_file", "--db", type=str, required=True)
args = parser.parse_args()

date_table = datetime.now().strftime("%Y%m%d_%S")

dbOp = CreateDB(args.db_file,date_table)
dbOp.create_table()

userOp = Users(args.json_file,args.db_file,date_table)
userOp.insert_user()