from sqlmodel import SQLModel, create_engine,Session
from todo.models.todo import *



file = "database.db"
url = f"sqlite:///{file}"
engine = create_engine(url)


def create_db():
    SQLModel.metadata.create_all(engine)


def add_todo(todo:NewTodo):
    ...

def retrieve_all_todo():
    ...

def retrieve_todo(id:int):
    ...

def delete_todo(id:int):
    ...

def delete_all_todo():
    ...

def update_todo(id:int, update: UpdateTodo):
    ...