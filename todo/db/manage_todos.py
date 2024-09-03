from sqlmodel import SQLModel, text, create_engine, Session, select
from todo.models.todo import *
import os

current_dir = os.path.dirname(__file__)

file = os.path.join(current_dir, "database.db")
url = f"sqlite:///{file}"
engine = create_engine(url)


def create_db():
    SQLModel.metadata.create_all(engine)


# No need for statement
def add_todo(new_todo: NewTodo) -> None:

    with Session(engine) as s:
        todo = Todo(content=new_todo.content, completed=False)
        s.add(todo)
        s.commit()


def retrieve_all_todo() -> list[TodoResponse]:

    with Session(engine) as s:
        statement = select(Todo)
        todos = [TodoResponse(content=t.content, completed=t.completed)
                 for t in s.exec(statement)]

    return todos


def retrieve_todo(id: int) -> None | TodoResponse:
    with Session(engine) as s:

        todo = s.get(Todo, id)

        return todo if todo is None else TodoResponse(content=todo.content, completed=todo.completed)


def delete_todo(id: int):
    with Session(engine) as s:
        todo = s.get(Todo, id)
        if todo is None:
            raise Exception()

        s.delete(todo)
        s.commit()


def delete_all_todo():
    with Session(engine) as s:

        s.exec(Todo.__table__.delete())
        # needed
        s.commit()


def update_todo(id: int, update: UpdateTodo):

    with Session(engine) as s:
        todo = s.get(Todo, id)

        if todo is None:
            raise Exception()

        todo.completed = update.completed
        todo.content = update.content
        s.add(todo)
        s.commit()
