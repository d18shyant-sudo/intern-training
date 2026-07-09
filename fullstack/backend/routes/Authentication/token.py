from datetime import datetime,timedelta
import jwt
def create_access_token(username:str,password:str):
    Secret_key ="ASDF"
    ALGORITHM ="HS256"
    if username == "user" and password == "123":
        payload = {"sub":username,"role":"admin","exp":datetime.utcnow()+timedelta(minutes=30)}
        token = jwt.encode(payload,Secret_key,algorithm=ALGORITHM)
        return {
            "access_token":token,
            "token_type":"bearer",
            "expire_at":payload["exp"]
            }
    return {
        "Error":"Invalid Credential"
    }