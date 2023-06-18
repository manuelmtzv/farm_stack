from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["https://localhost:300"]

app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)


@app.get("/")
def root():
    return {"message": "Root route"}


@app.get("/api/todo")
async def get_todo():
    return 1


@app.get("/api/todo/{id}")
async def get_todo_by_id(id):
    return id


@app.post("/api/todo/")
async def add_todo(todo):
    return 1


@app.put("/api/todo/{id}")
async def update_todo(id, data):
    return id


@app.delete("/api/todo/{id}")
async def delete_todo_by_id(id):
    return 1
