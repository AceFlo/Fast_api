# import uvicorn
# from fastapi import FastAPI, Path
# from typing import Optional
# from pydantic import BaseModel
# import os
# import json
#
# app = FastAPI()
#
#
# class Item(BaseModel):
#     name: str
#     price: int
#     brand: Optional[str] = None
#
#
# class UpdateItem(BaseModel):
#     name: Optional[str] = None
#     price: Optional[int] = None
#     brand: Optional[str] = None
#
#
# # file_name = "database.json"
# if os.path.exists(file_name):
#     print("File already exists")
# else:
#     with open(file_name, "x") as f:
#         print("File created")
#
#
# def write_mode():
#     with open(file_name, "w") as file:
#         json.dump()
#
#
# def read_mode():
#     with open(file_name, "r") as read:
#         file2 = json.load(read)
#     print(file2)
#
#
# @app.get("/")
# def home():
#     return read_mode()
#
#
# @app.get("/item/{item_id}")
# def get_item(item_id: int = Path(description="Item id ")):
#     read_mode()
#     return file_name[item_id]
#
#
# @app.get("/get-by-name")
# def get_item(name: Optional[str] = None):
#     read_mode()
#     for item_id in file_name:
#         if [item_id].name == name:
#             return file_name[item_id]
#     return {"Data": "Not found"}
#
#
# @app.post("/create_item/{item_id}")
# def create_item(item_id: int, item: Item):
#     f_write = write_mode()
#     if item_id in f_write:
#         return {"Error": "Item id already exists!"}
#     f_write[item_id] = item
#     return f_write[item_id]
#
#
# @app.put("/update_item/{item_id}")
# def update_item(item_id: int, item: UpdateItem):
#     with open(file_name, "w") as write:
#         if item_id not in write:
#             return {"Error": "Item id does not exists"}
#         if item.name is not None:
#             write["item_id"].name = item.name
#         if item.price is not None:
#             write["item_id"].price = item.price
#         if item.brand is not None:
#             write["item_id"].brand = item.brand
#     return write["item_id"]
#
#
# @app.delete("/delete_item")
# def delete_item(item_id: int):
#     with open(file_name, "w") as write:
#         if item_id not in write:
#             return {"Error": "Item id doesn't exist"}
#         del write[item_id]
#     return {"Successfully deleted!"}
#
#
# if __name__ == "__main__":
#     uvicorn.run("practise:app", host='0.0.0.0', port=8000, reload=True)
