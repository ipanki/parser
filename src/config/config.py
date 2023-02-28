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
    LAMODA_URL = 'https://www.lamoda.by/c/517/clothes-muzhskie-bryuki/'
    LAMODA_PRICE = 'x-product-card-description__price-single x-product-card-description__price-WEB8507_price_no_bold'
    LAMODA_DISCOUNT_PRICE = 'x-product-card-description__price-new x-product-card-description__price-WEB8507_price_no_bold'
    LAMODA_PAGES = 1

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


config = Config()



