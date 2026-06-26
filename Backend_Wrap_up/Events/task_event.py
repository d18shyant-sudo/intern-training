from sqlalchemy import event
from model import Task
import uuid
from datetime import datetime
@event.listens_for(Task,"before_insert")
def set_uuid(mapper,connection,target):
    if target.id is None:
        target.id = uuid.uuid4()
    if target.created_by is None:
        target.created_by = target.id
@event.listens_for(Task,"before_update")
def set_update_time(mapper,connection,target):
    target.updated_at = datetime.utcnow()
