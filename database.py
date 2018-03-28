import pymongo

__author__ = 'cyjm'


class Database(object):
    uri = "mongodb://127.0.0.1:27017"
    database = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.uri)
        Database.database = client["blog"]

    @staticmethod
    def insert(collection, data):
        Database.database[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.database[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.database[collection].find_one(query)
