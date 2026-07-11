from fastapi import Depends
from sqlalchemy.orm import Session
from engine.database import get_db
from schema.user import user
from database.user import create_detail,show_detail
from model.user import Detail

class service:
    def post_detail(detail:user.Create_detail,db:Session=Depends(get_db)):
        response = create_detail(detail,db)
        if isinstance(response,Detail):
            if detail.email == response.email:
                return []
        else:
            return response
        return response
    def get_detail(db:Session=Depends(get_db)):
       response = show_detail(db)
       if isinstance(response,list):
           if not response:
               return []
           else:
                return response
           return response