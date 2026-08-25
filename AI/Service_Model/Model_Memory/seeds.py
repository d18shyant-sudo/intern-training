from model.conversation import Conversation
from engine import session_local
import uuid
from datetime import datetime
db = session_local()
try:
    request_id = uuid.uuid4()
    user_id = uuid.uuid4()
    current_conversation = Conversation(id=request_id,user_id=user_id,model_name="claude",prompt="what is mean by global warming",response="global warming is a life threatening activity",created_by=user_id,created_at=datetime.now())
    db.add(current_conversation)
except Exception as e:
    db.rollback()
    print(e)
finally:
    db.commit()
    db.close()