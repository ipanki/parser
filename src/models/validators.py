from bson.objectid import ObjectId


def object_id_to_string(_id) -> str:
    if isinstance(_id, ObjectId):
        return str(_id)
    return _id
