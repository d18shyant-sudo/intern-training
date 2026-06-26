from sqlalchemy.orm import Session
from dependencies import get_db
import service
from schema import TaskResponse,TaskCreate
from  fastapi import FastAPI,Depends
import task_event
app = FastAPI()
@app.get("/tasks",response_model=list[TaskResponse])
def get_tasks_response(db:Session = Depends(get_db)):
    response =  service.get_tasks(db)
    return response
@app.get("/tasks/{title}",response_model=TaskResponse)
def get_task_response(title:str,db:Session = Depends(get_db)):
    response =  service.get_task(db,title)
    return response
@app.post("/tasks",response_model=TaskResponse)
def create_response(task:TaskCreate,db:Session = Depends(get_db)):
    response =  service.create_task(db,task)
    return response
@app.put("/tasks/{title}",response_model=TaskResponse)
def update_response(title:str,updated_task:TaskCreate,db:Session = Depends(get_db)):
    response =  service.update_task(db,title,updated_task)
    return response
@app.delete("/tasks/{title}",response_model=TaskResponse)
def delete_response(title:str,db:Session = Depends(get_db)):
    response =  service.delete_task(db,title)
    return response