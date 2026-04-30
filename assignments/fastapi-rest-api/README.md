# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

In this assignment, you will build a REST API using FastAPI and Python. You will learn how to create endpoints, validate request data with Pydantic models, and return structured JSON responses.

## 📝 Tasks

### 🛠️	Create Your First FastAPI Endpoints

#### Description
Set up a FastAPI app and create foundational endpoints so you can run and test your API locally.

#### Requirements
Completed program should:

- Create a FastAPI application instance in `starter-code.py`
- Include a `GET /` endpoint that returns a welcome JSON message
- Include a `GET /health` endpoint that returns `{ "status": "ok" }`
- Run successfully with Uvicorn on `http://127.0.0.1:8000`


### 🛠️	Build CRUD Endpoints for Tasks

#### Description
Implement a small in-memory task manager API. Add endpoints to create tasks, list all tasks, and fetch a single task by ID.

#### Requirements
Completed program should:

- Define a Pydantic model for task creation input (`title`, `completed`)
- Define a response model that includes `id`, `title`, and `completed`
- Implement `POST /tasks` to create and return a new task
- Implement `GET /tasks` to return all tasks
- Implement `GET /tasks/{task_id}` to return one task or a 404 error when not found


### 🛠️	Add Update and Delete Operations

#### Description
Complete your REST API by adding update and delete behavior for existing tasks.

#### Requirements
Completed program should:

- Implement `PUT /tasks/{task_id}` to update task fields
- Implement `DELETE /tasks/{task_id}` to remove a task
- Return appropriate status codes (`200`, `201`, `404`)
- Return clear JSON error messages for invalid task IDs
