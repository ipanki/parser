from pymongo import mongo_client
from src.config.config import config


client = mongo_client.MongoClient(config.DATABASE_URL)
db = client[config.MONGO_INITDB_DATABASE]
lamoda_db = db['lamoda']
twitch_db = db['twitch']

