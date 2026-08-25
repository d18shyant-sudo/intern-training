from model.conversation import Conversation
from schema.conversation import ConversationRequest,ConversationHistory
from sqlalchemy.orm import Session
import logging
logging.basicConfig(level=logging.WARNING)
class Conversation_Repository:
    def post_conversation(request:ConversationRequest,db:Session):
        try:
            current_conversation = Conversation()
            for field,value in request.model_dump().items():
                setattr(current_conversation,field,value)
            db.add(current_conversation)
            db.commit()
            db.refresh(current_conversation)
            return current_conversation
        except Exception as e:
            db.rollback()
            logging.warning(e)
            return []
                 
    def get_conversation(req_id:ConversationHistory,db:Session):
        try:
            result = db.query(Conversation).filter(Conversation.user_id == req_id.id).all()
            return result
        except:
            db.rollback()
            return []