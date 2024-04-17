from typing import Optional
from sqlmodel import (Session, SQLModel, Field, create_engine,
                      select)


class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    status: str = "todo"

    person_id: int = Field(foreign_key="person.id")


engine = create_engine("sqlite:///db.db")
SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    query = select(Todo)
    print(session.exec(query).all())
