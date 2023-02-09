from flask import Flask, request # will carry all the request data ( cookies , header , body , of your request)
from app.database import task # we are importing task.py (lowercase means its a module)

app = Flask(__name__) # (__name__) = app 


@app.get("/ping")
@app.get("/")
def get_ping():
    out = {
        "ok": True,
        "message": "pong",  
    }
    return out

@app.get("/tasks")
def get_all_tasks():
    tasks = task.scan()
    out = {
        "ok": True,
        "tasks": tasks 
    }
    return out

@app.get("/tasks/<int:pk>")
def get_task_by_id(pk):
    selected_task = task.select_by_id(pk)
    out = {
        "ok": True,
        "task": selected_task[0]
    }
    return out 
    
@app.post("/tasks")
def create_task():
    raw_data = request.json
    task.insert(raw_data)
    return "", 204

@app.put("/tasks/<int:pk>")
def update_task(pk):
    raw_data = request.json
    task.update(raw_data, pk)
    return "", 204

@app.delete("/tasks/<int:pk>")
def delete_task(pk):
    task.delete(pk)
    return "", 204

