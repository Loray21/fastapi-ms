import models
from database import engine, SessionLocal
from fastapi import FastAPI, Depends, HTTPException, Path
from typing import Annotated
from sqlalchemy.orm import Session
from models import Todos
from starlette import status
from pydantic import BaseModel, Field
from routers import auth, todos


app = FastAPI()
models.Base.metadata.create_all(bind=engine)


app.include_router(auth.router)
app.include_router(todos.router)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependecy = Annotated[Session, Depends(get_db)]


class TodoRequest(BaseModel):
    title: str = Field(minlength=3)
    description: str = Field(minlength=3, maxlength=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool


@app.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependecy):
    return db.query(Todos).all()


@app.get("/todo/{todoid}", status_code=status.HTTP_200_OK)
async def get_by_id(db: db_dependecy, todoid: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todoid).first()
    if todo_model:
        return todo_model
    else:
        raise HTTPException(status_code=404, detail="Not found")




@app.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependecy, todo_request: TodoRequest):
    db.add(Todos(**todo_request.dict()))
    db.commit()


@app.put("/todo", status_code=status.HTTP_204_NO_CONTENT)
async def edit_todo(db: db_dependecy,
                    todo_int: int,
                    todo_request: TodoRequest):
    request = Todos(**todo_request.dict())
    found = False
    for todo in db.query(Todos).all():
        if todo.id == todo_int:
            found = True
            todo.title = request.title
            todo.description = request.description
            todo.priority = request.priority
            todo.complete = request.complete
            db.commit()
    if not found:
        raise HTTPException(status_code=404, detail="Not found")


@app.delete("/todo", status_code=status.HTTP_200_OK)
async def delete(db: db_dependecy,
                 todo_int: int):
    todo = db.query(Todos).filter(Todos.id == todo_int).delete()
    db.commit()
    if todo == 0:
        raise HTTPException(status_code=404, detail="Not found")
