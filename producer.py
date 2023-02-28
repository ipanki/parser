import asyncio
from json import dumps
from kafka import KafkaProducer
from src.parsers.parser_lamoda import ParserLamoda
from src.parsers.parser_twitch import TwitchParser
from consumer import insert_streams_twitch, insert_clothes_lamoda


def _connect_kafka():
    producer = KafkaProducer(
        api_version=(0, 11, 5),
        bootstrap_servers=['localhost:29092'],
        value_serializer=lambda x: dumps(x).encode('utf-8')
    )
    return producer


def _send_data_lamoda(data):
    producer = _connect_kafka()
    producer.send('lm', value=data)


def _send_data_twitch(data):
    producer = _connect_kafka()
    producer.send('tw', value=data)


def run_parser_twitch():
    parser_twitch = TwitchParser()
    data = parser_twitch.parse_twitch()
    _send_data_twitch(data)
    insert_streams_twitch()


def run_parser_lamoda():
    parser_lamoda = ParserLamoda()
    data = asyncio.run(parser_lamoda.parse_clothes())
    _send_data_lamoda(data)
    insert_clothes_lamoda()

