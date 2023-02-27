from src.dao.lamoda_dao import LamodaDao
from src.models.database import connect_db


class LamodaService:
    def __init__(self):
        self.__dao = LamodaDao(connect_db())

    def get_all_clothes(self):
        return self.__dao.get_elements()

    def create_thing_lamoda(self, thing):
        return self.__dao.create(thing)

    def get_one_thing(self, _id):
        return self.__dao.get_element(_id)

    def delete_thing(self, _id):
        return self.__dao.delete_element(_id)
