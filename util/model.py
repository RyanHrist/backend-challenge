from abc import abstractmethod


class Model:
    _dao = None
    _collection: dict = dict()

    def __init__(self, dao, collection: dict = None):
        Model._dao = dao()
        Model._collection = collection or dict()

    @abstractmethod
    def get_by_id(self, _id: str) -> 'Model':
        return Model

    @abstractmethod
    def save(self, params: dict) -> 'Model':
        return Model
