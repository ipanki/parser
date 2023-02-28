from pymongo import mongo_client
from src.config.config import config


def connect_db():
    client = mongo_client.MongoClient(config.database_url)
    db = client[config.mongo_initdb_database]
    return db

