from pymongo import mongo_client
from src.config.config import config


def connect_db():
    client = mongo_client.MongoClient(config.DATABASE_URL)
    print('Connected to MongoDB...')
    db = client[config.MONGO_INITDB_DATABASE]
    return db

