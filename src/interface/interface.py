from abc import ABC, abstractmethod


class InterfaceDaoLamoda(ABC):

    @abstractmethod
    def drop_collection(self):
        pass

    @abstractmethod
    def create(self, element):
        pass

    @abstractmethod
    def get_elements(self):
        pass

    @abstractmethod
    def get_element(self, _id):
        pass

    @abstractmethod
    def insert_elements(self, elements):
        pass

    @abstractmethod
    def delete_element(self, _id):
        pass
