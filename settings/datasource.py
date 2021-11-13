from pymongo import MongoClient


def get_mongo_db(host, port, db_name):
    client = MongoClient(host, port)
    # client = MongoClient('localhost', 27017)
    # db = client.stock_alert
    return client.get_database(name=db_name)
