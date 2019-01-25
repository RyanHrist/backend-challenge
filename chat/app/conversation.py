from chat.app.conversation_dao import ConversationDao
from util.model import Model


class ConversationModel(Model):
    def __init__(self, collection: dict={}):
        super().__init__(ConversationDao, collection)

    def get_by_id(self, _id: str):
        dao = ConversationDao()
        message = dao.get_by_id(_id)
        return message


    def save(self, params: dict):
        dao = ConversationDao()
        dao.save(params)