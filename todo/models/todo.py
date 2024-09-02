from sqlmodel import SQLModel, Field
from pydantic import BaseModel


class Todo(SQLModel, table=True):

    id: int | None = Field(default=None, primary_key=True)
    content:str
    completed: bool


class NewTodo(BaseModel):

    content: str


class UpdateTodo(BaseModel):
    completed: bool