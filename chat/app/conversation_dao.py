from util.dao import DAO
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import datetime


class ConversationDao(DAO):
    def __init__(self):
        self._db = None
        self._logger = print
        self._db = self._get_connection()

    @classmethod
    def _get_connection(cls):
        database_name = 'database'
        table = 'converations'

        client = MongoClient("mongodb://localhost:27017/")
        try:
            conn = client.get_database(database_name)
        except ConnectionFailure:
            raise

        return conn.get_collection(table)

    def save(self, params: dict):
        collection = self._get_connection()

        now = datetime.datetime.now()
        created = now.strftime("%Y-%m-%d %H:%M")

        found_id = self.get_by_id(params["conversation_id"])
        # If conversation exists, update
        if found_id:
            collection.update(
                {"id": params["conversation_id"]},
                {
                    "$push": {
                        "messages": {
                            "sender": params["sender"],
                            "message": params["message"],
                            "created": created
                        }
                    }
                }
            )
        # If conversation does not exist, create new
        else:
            collection.insert_many([
                {"id": params["conversation_id"],
                 "messages": [{
                     "sender": params["sender"],
                     "message": params["message"],
                     "created": created
                 }]}
            ])

    def get_by_id(self, _id: str):
        collection = self._get_connection()
        find_query = {"id": _id}
        result = collection.find(find_query)
        for x in result:
            print(0)
            if x:
                return x
