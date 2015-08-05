import sqlite3
import pandas as pd
__author__ = 'rain'


class Repository(object):
    """
    List keys:
        - desktops
    """
    data = {}

    def __init__(self):
        pass

    @staticmethod
    def get_data(key):
        if Repository.data.has_key(key):
            return Repository.data[key]
        else:
            return Repository.load_data(key)

    @staticmethod
    def set_data(key, value):
        Repository.data[key] = value

    @staticmethod
    def load_data(key):
        if key == 'desktops':
            con = sqlite3.connect('../input/database.sqlite')
            value = pd.read_sql('select * from cookies', con)
            Repository.set_data(key, value)
            return value