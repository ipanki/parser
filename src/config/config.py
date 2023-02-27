from pydantic import BaseSettings


class Config(BaseSettings):
    MONGO_INITDB_ROOT_USERNAME: str
    MONGO_INITDB_ROOT_PASSWORD: str
    MONGO_INITDB_DATABASE: str
    DATABASE_URL: str
    STREAMS: str
    AUTH_URL: str
    CLIENT_ID: str
    CLIENT_SECRET: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


config = Config()



