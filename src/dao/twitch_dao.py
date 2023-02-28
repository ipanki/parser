from typing import Dict

from fastapi import Body, Depends, HTTPException, status
from bson.objectid import ObjectId
from src.models.twtich.models import Streams, StreamsCreateUpdate, StreamsResponse
from src.models.database import connect_db
from src.interface.interface import InterfaceDao


class TwitchDao(InterfaceDao):
    def __init__(self, session: Depends(connect_db)):
        self.__session = session
        self.__db = self._get_collection(session)

    def _get_collection(self, session):
        return session['twitch']

    def drop_collection(self):
        return self.__db.drop()

    def create(self, stream: StreamsCreateUpdate = Body(...)) -> Dict[str, str]:
        new_stream = self.__db.insert_one(stream.dict())
        return {"_id": str(new_stream.inserted_id), **stream.dict()}

    def get_elements(self) -> StreamsResponse:
        return StreamsResponse(streams=list(self.__db.find()))

    def get_element(self, _id: str):
        element = self.__db.find_one({'_id': ObjectId(_id)})
        if element is not None:
            element['_id'] = str(element['_id'])
            return element
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Stream with ID {_id} not found')

    def insert_elements(self, elements):
        return self.__db.insert_many(elements)

    def delete_element(self, _id):
        data = self.__db.find_one({'_id': ObjectId(_id)})
        if data is not None:
            self.__db.delete_one({'_id': ObjectId(_id)})
            return {"message": f"Thing with ID {_id} was deleted"}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Stream with ID {_id} not found')


