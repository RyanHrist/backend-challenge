from abc import ABC, abstractmethod


class DAO(ABC):
    def __call__(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_by_id(self, _id: str) -> dict:
        return dict()

    @abstractmethod
    def save(self, params: dict) -> None:
        return