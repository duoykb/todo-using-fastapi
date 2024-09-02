from fastapi import APIRouter, HTTPException, status
from todo.models.todo import *
from todo.db import manage_todos


route = APIRouter()


def logger():
    pass


#POST
@route.post("/")
async def add_todo(new_todo: NewTodo) -> dict:
    manage_todos.add_todo(new_todo)

    return {
        "message" : "todo was added."
    }


#GET
@route.get("/")
async def retrieve_all_todo()-> list[TodoResponse]:
    return manage_todos.retrieve_all_todo()


@route.get("/{id}")
async def retrieve_todo(id: int) -> TodoResponse:
    
    todo = manage_todos.retrieve_todo(id)

    if not todo:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="todo not found.")
    
    return todo


#UPDATE
@route.put("/{id}")
async def update_todo(id:int, update: UpdateTodo) -> dict:
    
    try:
        manage_todos.update_todo(id, update)
    except Exception:    
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="todo not found.")
    
    return { 
        "message" : "todo was updated."
    }


#DELETE
@route.delete("/")
async def delete_all() -> dict:
    manage_todos.delete_all_todo()
    return {
            "message" : "todos were cleared."
        }

@route.delete("/{id}")
async def delete_todo(id:int):
    
    try:
        manage_todos.delete_todo(id)
    except Exception:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="todo not found")
    
    return {"message": "todo was deleted."}