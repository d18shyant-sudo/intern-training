from sqlalchemy import event
from model import Detail
import uuid
@event.listens_for(Detail,"before_insert")
def set_uuid(mapper,connection,target):
    if target.id is None:
        target.id = uuid.uuid4()
    if target.created_by is None:
        target.created_by = target.id
        