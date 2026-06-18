from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return { "message":"Hello Welcome!"}

@app.get("/hello/{user}")
def greeting(user:str):
   return {"message": f"Hello {user} !"}
