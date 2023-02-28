from src.dao.twitch_dao import TwitchDao
from src.models.database import connect_db


class TwitchService:
    def __init__(self):
        self.__dao = TwitchDao(connect_db())

    def get_all_streams(self):
        return self.__dao.get_elements()

    def create_stream(self, stream):
        return self.__dao.create(stream)

    def get_one_stream(self, _id):
        return self.__dao.get_element(_id)

    def delete_stream(self, _id):
        return self.__dao.delete_element(_id)
