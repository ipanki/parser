from pymongo import mongo_client
from src.config import config


def connect_db():
    client = mongo_client.MongoClient(config.Config.DATABASE_URL)
    print('Connected to MongoDB...')
    db = client[config.Config.MONGO_INITDB_DATABASE]
    return db

