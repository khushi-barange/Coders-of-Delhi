import json

def load_data(filename):
    with open(filename, "r") as file:
        return json.load(file)

def clean_data(data):
    data["users"] = [u for u in data["users"] if u["name"].strip()]

    for u in data["users"]:
        u["friends"] = list(set(u["friends"]))

    data["users"] = [u for u in data["users"] if u["friends"] or u["liked_pages"]]

    unique_pages = {}
    for p in data["pages"]:
        unique_pages[p["id"]] = p
    data["pages"] = list(unique_pages.values())

    return data
