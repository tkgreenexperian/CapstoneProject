from src.db.library_db import LibraryDatabase


def test_database_connection():
    db = LibraryDatabase()
    assert db.connection is not None


def test_create_table():
    db = LibraryDatabase()
    db.create_table()
    assert True