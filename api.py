import uvicorn
from fastapi import FastAPI, Path, status
from typing import Optional
import json_functions
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    roll_num: int
    price: Optional[float] = None


class UpdateItem(BaseModel):
    name: Optional[str] = None
    roll_num: Optional[int] = None
    price: Optional[float] = None


@app.get("/show_items")
def info():
    return json_functions.show_data()


@app.get("/items/{item_id}", status_code=status.HTTP_200_OK)
def get_item(item_id: int = Path(description="The id of the item you'd like to view")):
    data = json_functions.show_data()
    if item_id < len(data):
        return data[item_id]
    else:
        return {"Error": "Item id doesnt exist"}


@app.get("/get_by_name/{name}")
def get_item(name: str):
    data = json_functions.show_data()
    for items in data:
        if items.get("name") == name:
            return items
    return {"Data": "Not Found"}


@app.post("/create_item/")
def create_item(item: Item):
    data = json_functions.show_data()
    if len(data) == 0:
        new_data = json_functions.create_file([item.dict()])
    else:
        new_data = json_functions.add_new_data(item.dict())
    return new_data


@app.put("/Update_Item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    data = json_functions.show_data()
    if item_id > len(data):
        return {"Error": "item id doesn't exist"}
    else:
        json_functions.update_data(item_id, item.dict())
        return json_functions.show_data()[item_id]


@app.delete("/delete_item")
def delete_item(item_id: int):
    data = json_functions.show_data()
    if item_id >= len(data):
        return {"Error": "Item id doesnt exist"}
    else:
        json_functions.delete_file(item_id)
        return {"i'd deleted"}


if __name__ == "__main__":
    uvicorn.run("api:app", host='0.0.0.0', port=8000, reload=True)
