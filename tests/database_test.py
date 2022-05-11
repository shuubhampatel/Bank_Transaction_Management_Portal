"""database dir. existence check"""
import os


def test_database_directory():
    """database check"""
    root = os.path.dirname(os.path.abspath(__file__))
    dbdir = os.path.join(root, '../database')
    assert os.path.exists(dbdir) is True

# def test_database_file():
#    root = os.path.dirname(os.path.abspath(__file__))
#    database = os.path.join(root, '../database/db2.sqlite')
#    assert os.path.exists(database) is True