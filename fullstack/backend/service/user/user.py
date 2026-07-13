from fastapi import Depends
from sqlalchemy.orm import Session
from engine.database import get_db
from schema.user.user import Create_detail
from database.user import create_detail,show_detail,delete_detail,update_detail
from model.user.user import Detail

class service:
    def post_detail(detail:Create_detail,db:Session=Depends(get_db)):
        response = create_detail(detail,db)      
        if response == True:
                return True
        if isinstance(response,Detail):
            return response
        return response
    def get_detail(db:Session=Depends(get_db)):
       response = show_detail(db)
       if  response == False:
        return False
       elif isinstance(response,list):
                return response
       return response
    def delete_detail(email:str,db:Session=Depends(get_db)):
        response = delete_detail(email,db)
        if response == False:
            return False
        if isinstance(response,Detail):
         return response
        return response
    def update_detail(email:str,detail:Create_detail,db:Session=Depends(get_db)):
        response = update_detail(email,detail,db)
        if response == False:
            return False
        if isinstance(response, Detail):
            return response
        return response