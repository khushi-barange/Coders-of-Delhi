def most_connected_user(data):
    user = max(data["users"], key=lambda u: len(u["friends"]))
    return user["name"], len(user["friends"])

def most_popular_page(data):
    page_count = {}
    for u in data["users"]:
        for p in u["liked_pages"]:
            page_count[p] = page_count.get(p, 0) + 1

    most_liked_page = max(page_count, key=page_count.get)
    page_name = next(p["name"] for p in data["pages"] if p["id"] == most_liked_page)
    return page_name, page_count[most_liked_page]
