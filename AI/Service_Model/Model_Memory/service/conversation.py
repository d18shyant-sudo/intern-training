from repository.conversation import Conversation_Repository
from schema.conversation import ConversationRequest,ConversationHistory
from sqlalchemy.orm import Session
import logging
logging.basicConfig(level=logging.WARNING)
class Service:
    def post_conversation(request:ConversationRequest,db:Session):
        try:
            result = Conversation_Repository.post_conversation(request,db)
            return result
        except Exception as e:
            logging.warning(e)
            return []
           
    def get_conversation(req_id:ConversationHistory,db:Session):
        try:
            result = Conversation_Repository.get_conversation(req_id,db)
            return result
        except:
            return []  