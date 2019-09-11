
import Ddb 

def test_database_creation():
    db = Ddb.Database("data.json")

def test_table_creation():
    db = Ddb.Database("data.json")
    table = db.table('Words')


# def test_hello():
#     Database = Ddb.Database()
#     print("hello world!")