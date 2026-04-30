"""Starter code for Building REST APIs with FastAPI.

Run locally:
    uvicorn starter-code:app --reload
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task API Starter")


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


class Task(TaskCreate):
    id: int


# In-memory storage for this assignment.
tasks: list[Task] = []
next_id = 1


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Welcome to your FastAPI assignment API!"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(payload: TaskCreate) -> Task:
    global next_id
    task = Task(id=next_id, **payload.model_dump())
    tasks.append(task)
    next_id += 1
    return task


@app.get("/tasks", response_model=list[Task])
def list_tasks() -> list[Task]:
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, payload: TaskCreate) -> Task:
    for index, task in enumerate(tasks):
        if task.id == task_id:
            updated = Task(id=task_id, **payload.model_dump())
            tasks[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int) -> dict[str, str]:
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")
