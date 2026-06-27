from sqlalchemy.orm import Session
from model import Task
from schema import TaskCreate
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime
def create_task(db:Session,task:TaskCreate):
    try:
        task_in_db = db.query(Task).filter(Task.title==task.title).first()
        if task_in_db:
           return JSONResponse(status_code=400,content={"error":"Task is already exists"})
        new_task = Task(title=task.title,description=task.description,completed=task.completed)
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        new_task.created_by = new_task.id
        db.commit()
        return new_task
    except Exception as e:
         db.rollback()
         return JSONResponse(status_code=400,content={"error":str(e)})
def get_tasks(db:Session):
    try:
        task_in_db = db.query(Task).all()
        if not task_in_db:
            return JSONResponse(status_code=404,content={"error":"No task is added"})
        return task_in_db
    except Exception as e:
        return JSONResponse(status_code=404,content=str(e))
def get_task(db:Session,title:str):
    try:
        task_in_db = db.query(Task).filter(Task.title==title).first()
        if not task_in_db:
            return JSONResponse(status_code=404,content={"error":"No such task is exists"})
        return task_in_db
    except Exception as e:
        return JSONResponse(status_code=404,content=str(e))
def update_task(db:Session,title:str,updated_task:TaskCreate):
    try:
        task_in_db = db.query(Task).filter(Task.title==title).first()
        if not task_in_db:
            return JSONResponse(status_code=400,content={"error":"No such task is exists"})
        task_in_db.title = updated_task.title
        task_in_db.description = updated_task.description
        task_in_db.completed = updated_task.completed
        task_in_db.updated_by = task_in_db.id
        # task_in_db.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(task_in_db)
        return task_in_db
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=400,content=str(e))
def delete_task(db:Session,title:str):
    try:
        task_in_db = db.query(Task).filter(Task.title==title).first()
        if not task_in_db:
            return JSONResponse(status_code=404,content={"error":"No such task is exist"})
        task_in_db.is_active = False
        task_in_db.is_delete = True
        db.commit()
        return task_in_db
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=404,content=str(e))