from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app = FastAPI()
tasks =[]
class TaskCreate(BaseModel):
    title:str
    description:str
    completion:bool = False
class TaskResponse(BaseModel):
    id : int
    title:str
    description:str
    completion:bool
@app.get("/tasks",response_model=list[TaskResponse])
def get_tasks():
     return tasks
@app.get("/tasks/{id}")
def get_task(id:int):
    for task in tasks:
        if task["id"] ==  id:
            return task
    raise HTTPException(
        status_code=404,
        detail="Task Not Found"
    )
@app.post("/tasks",response_model=TaskResponse,status_code=201)
def post_task(id:int,task:TaskCreate):
    task_id = len(tasks)+1
    new_task = {
        "id":task_id,
        "title":task.title,
        "description":task.description,
        "completion":task.completion
    }
    tasks.append(new_task)
    return new_task
@app.put("/tasks/{id}",response_model=TaskResponse)
def put_task(id:int,updated_task:TaskCreate):
    for task in tasks:
        if task["id"] == id:
            task["title"] = updated_task.title
            task["description"] = updated_task.description
            task["completion"] = updated_task.completion
            return task
    raise HTTPException(
        status_code=404,
        detail="No such task"
    )
@app.delete("/tasks/{id}",status_code=200)
def delete_task(id:int):
    for index,task in enumerate(tasks):
        if task["id"] ==  id:
           deleted =  tasks.pop(index)
           return {
               "message":"task deleted",
               "task":deleted
           }
    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )