from Fast_api_database import schema
from schema import Users, UpdateUsers
import uvicorn
from fastapi import FastAPI, Depends, UploadFile, File
from sqlalchemy.orm import Session
import models
from database import engine, get_db

app = FastAPI()


@app.get("/show_items")
def info(db: Session = Depends(get_db)):
    return db.query(models.User).all()


@app.get("/show_item/{item_id}", response_model=schema.UserParent)
def get_by_id(item_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == item_id).first()
    return db_user


@app.post("/create_item", response_model=schema.UserParent)
def create_user(user: Users, db: Session = Depends(get_db)):
    models_users = models.User()
    models_users.name = user.name
    models_users.email = user.email
    models_users.password = user.password
    db.add(models_users)
    db.commit()
    return user


@app.put("/update_item/{user_id}")
def update_item(user_id: int, user: UpdateUsers, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        return {"error": f"User with id {user_id} does not exist."}
    if user.name is not None:
        db_user.name = user.name
    if user.email is not None:
        db_user.email = user.email
    if user.password is not None:
        db_user.password = user.password
    db.commit()
    db.refresh(db_user)

    return {"message": "User updated successfully"}


@app.post("/upload_file/")
def upload_file(*, file: UploadFile = File()):
    file_size = file.file.read()
    return {"File_name" : file.filename,
            "file_size" : len(file_size)
            }


@app.delete("/delete_id/{user_id}")
def delete_id(user_id: int, db: Session = Depends(get_db)):
    models_users = db.query(models.User).filter(models.User.id == user_id)
    if models_users is None:
        return f"{user_id} doesn't exist"
    models_users.delete()
    db.commit()
    return {"Data deleted successfully!"}


if __name__ == "__main__":
    models.Base.metadata.create_all(bind=engine)
    uvicorn.run("api_database:app", host='0.0.0.0', port=8000, reload=True)
