import uvicorn
from fastapi import FastAPI
from todo.routes import todo
from todo.db import manage_todos

app = FastAPI()

# Add routes

app.include_router(todo.route)

# ...

config = uvicorn.Config("__main__:app", port=5000, host="0.0.0.0",  log_level="info")
server = uvicorn.Server(config)

if __name__ == "__main__":

    manage_todos.create_db()
    server.run()