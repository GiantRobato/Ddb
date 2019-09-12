
import Ddb 

def test_database_creation():
    db = Ddb.Database("data.json")

def test_table_creation_and_insertion():
    db = Ddb.Database("data.json")
    table = db.table('Words')
    table.insert({"Hello" : "World"})
    table.insert({"Up" : "Down"})

def test_multiple_table_creation():
    db = Ddb.Database("data.json")
    table = db.table('MyTable')
    table.insert({"key" : "value"})
    table2 = db.table('OtherTable')
    table2.insert({"key" : "value"})

def test_all():
    db = Ddb.Database("data.json")
    table = db.table('Words')
    documents = [
        {"Hello" : "World"},
        {"Up" : "Down"},
        {"Left" : "Right"},
    ]
    for doc in documents:
        table.insert(doc)
    assert documents == table.all()