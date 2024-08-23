import json
import os


def create_file(new_data):
    with open("json_data.json", "w") as file:
        json.dump(new_data, file, indent=4)
    return show_data()


def add_new_data(new_data):
    with open("json_data.json", "r+") as file:
        data = json.load(file)
        data.append(new_data)
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
    return show_data()


new_file = []


def show_data():
    if os.path.exists("json_data.json"):
        with open("json_data.json", "r+") as file:
            content = file.read()
            if not content:
                return new_file
            else:
                data = json.loads(content)
                return data
    else:
        with open("json_data.json", "w") as file:
            json.dump(new_file, file, indent=4)
            return new_file


def update_data(index, new_data):
    with open("json_data.json", "r+") as file:
        data = json.load(file)
        if 0 <= index < len(data):
            data[index].update(new_data)
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
        else:
            return {"Error": "Index out of range!"}


def delete_file(index):
    with open("json_data.json", "r") as file:
        data = json.load(file)
        if index < len(data):
            data_exist = data[index]
            data.remove(data_exist)
    with open("json_data.json", "w") as updated_data:
        json.dump(data, updated_data, indent=4)


