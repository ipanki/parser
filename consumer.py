from json import loads
from kafka import KafkaConsumer
from src.di.lamoda_di import LamodaService
from src.di.twitch_di import TwitchService


def insert_clothes_lamoda():
    lamoda = LamodaService()
    consumer = KafkaConsumer(
        'lm',
        api_version=(0, 11, 5),
        bootstrap_servers=['localhost:29092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='1',
        value_deserializer=lambda x: loads(x.decode('utf-8'))
    )
    consumer.subscribe(topics=["lm"])
    lamoda.drop_collection()

    for message in consumer:
        lamoda.insert_clothes(message.value)


def insert_streams_twitch():
    twitch = TwitchService()
    consumer = KafkaConsumer(
        'tw',
        api_version=(0, 11, 5),
        bootstrap_servers=['localhost:29092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='2',
        value_deserializer=lambda x: loads(x.decode('utf-8'))
    )
    consumer.subscribe(topics=["tw"])
    twitch.drop_collection()

    for message in consumer:
        twitch.insert_streams(message.value)
