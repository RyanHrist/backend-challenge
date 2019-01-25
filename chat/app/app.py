import uuid
import traceback

from bson.json_util import dumps

from flask import Flask
from flask import request
from flask_restful import Resource, Api
from chat.app.conversation import ConversationModel

app = Flask(__name__)
api = Api(app)

class Converation(Resource):
    def get(self, conversation_id: str):
        model = ConversationModel()
        try:
            uuid.UUID(conversation_id, version=4)
            conversation = model.get_by_id(conversation_id)
            if conversation:
                conversation = dumps(conversation)
                return conversation, 200
            else:
                return {'message': f"User with ID {conversation_id} does not exist."}, 404
        except ValueError:
            traceback.print_exc()
        except Exception:
            traceback.print_exc()
            raise


class Message(Resource):
    def post(self):
        new_message = {}
        for args in request.args:
            new_message[args] = request.args.get(args)

        conversation_id = new_message["conversation_id"]
        model = ConversationModel()
        try:
            uuid.UUID(conversation_id, version=4)
            model.save(new_message)
            return {'message': 'New message sent by ' + new_message["sender"] +
                               ' that reads: ' + new_message["message"] + '. Convo ID: ' +
                    conversation_id}, 201
        except ValueError:
            traceback.print_exc()
            return {'message': 'Invalid ID Format: ' + new_message["conversation_id"]}, 400
        except Exception:
            traceback.print_exc()
            raise


# Add the resource endpoint to the API
api.add_resource(Converation, '/conversations/<string:conversation_id>')
api.add_resource(Message, '/messages')

