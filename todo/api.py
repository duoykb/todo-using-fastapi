import uvicorn
import uvicorn.config
from fastapi import FastAPI
from todo.routes import todo

app = FastAPI()

#Add routes

app.include_router(todo.route)

#...
app.include_router

config = uvicorn.Config("api:app", port=5000, host="0.0.0.0", log_config="info")
server = uvicorn.Server(config)

server.run()