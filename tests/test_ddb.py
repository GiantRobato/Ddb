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


def test_search_eq():
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
    assert [] == table.search(Word.flavor == "spicy")

def test_search_comparisons():
    db = Ddb.Database("data.json")
    table = db.table("Scores")
    documents = [
        {"name" : "Galaga", "score": 50, "player": "me2"},
        {"name" : "Galaga", "score": 100, "player": "me"},
        {"name" : "Galaga", "score": 1337, "player": "m3"},
        {"name" : "Bomberman", "score": 808135, "player": "bomberwoman"},
        {"name" : "Bomberman", "score": 803834342, "player": "hacker"}
    ]
    for doc in documents:
        table.insert(doc)
    Entry = Ddb.Query()
    assert len(table.search(Entry.score != 100)) == 4
    assert len(table.search(Entry.score < 1000)) == 2
    assert len(table.search(Entry.score < 2000)) == 3
    assert len(table.search(Entry.score <= 1337)) == 3
    assert len(table.search(Entry.score > 9000)) == 2
    assert len(table.search(Entry.score > 1e7)) == 1
    assert len(table.search(Entry.score >= 808135)) == 2
    assert len(table.search(Entry.name._in(["Galaga"]))) == 3
    assert len(table.search(Entry.name._in(["Space Invaders"]))) == 0
    assert len(table.search(Entry.player._contains("me"))) == 2