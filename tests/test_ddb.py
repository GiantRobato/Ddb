import Ddb


def test_database_creation():
    db = Ddb.Database("data.json")


def test_table_creation_and_insertion():
    db = Ddb.Database("data.json")
    table = db.table("Words")
    table.insert({"Hello": "World"})
    table.insert({"Up": "Down"})


def test_multiple_table_creation():
    db = Ddb.Database("data.json")
    table = db.table("MyTable")
    table.insert({"key": "value"})
    table2 = db.table("OtherTable")
    table2.insert({"key": "value"})


def test_all():
    db = Ddb.Database("data.json")
    table = db.table("Words")
    documents = [{"Hello": "World"}, {"Up": "Down"}, {"Left": "Right"}]
    for doc in documents:
        table.insert(doc)
    assert documents == table.all()


def test_search():
    db = Ddb.Database("data.json")
    table = db.table("Words")
    documents = [
        {"name": "apple", "type": "fruit"},
        {"name": "carrot", "type": "vegtable"},
        {"name": "pear", "type": "fruit"},
        {"name": "orange", "type": "fruit"},
    ]
    expected_fruits = [
        {"name": "apple", "type": "fruit"},
        {"name": "pear", "type": "fruit"},
        {"name": "orange", "type": "fruit"},
    ]
    expected_vegtables = [
        {"name": "carrot", "type": "vegtable"},
    ]
    for doc in documents:
        table.insert(doc)

    Word = Ddb.Query()
    assert expected_fruits == table.search(Word.type == "fruit")
    assert expected_vegtables == table.search(Word.type == "vegtable")
    # assert expected_fruits == words

