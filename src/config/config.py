from pydantic import BaseSettings


class Config(BaseSettings):
    mongo_initdb_root_username: str
    mongo_initdb_root_password: str
    mongo_initdb_database: str
    database_url: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


class TwitchConfig(BaseSettings):
    streams: str
    auth_url: str
    client_id: str
    client_secret: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


class LamodaConfig(BaseSettings):
    url = 'https://www.lamoda.by/c/517/clothes-muzhskie-bryuki/'
    price = 'x-product-card-description__price-single x-product-card-description__price-WEB8507_price_no_bold'
    discount_price = 'x-product-card-description__price-new x-product-card-description__price-WEB8507_price_no_bold'
    pages = 1

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


config = Config()
lamoda_config = LamodaConfig()
twitch_config = TwitchConfig()



