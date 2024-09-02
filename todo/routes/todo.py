from fastapi import APIRouter, HTTPException
from todo.models.todo import *

route = APIRouter()


#POST
@route.post("/")
async def add_todo(new_todo: NewTodo) -> dict:
    ...

#GET
@route.get("/")
async def retrieve_all_todo()-> dict:
    return {"msg" : "hello there"}


@route.get("/{id}")
async def retrieve_todo() -> dict:
    ...

#UPDATE
@route.put("/{id}")
async def update_todo(id:int, update: UpdateTodo):
    ...


#DELETE
@route.delete("/")
async def delete_all():
    ...


@route.delete("/{id}")
async def delete_todo(id:int):
    ...