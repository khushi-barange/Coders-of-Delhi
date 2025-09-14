def find_people_you_may_know(user_id, data):
    user_friends = {u["id"]: set(u["friends"]) for u in data["users"]}
    if user_id not in user_friends:
        return []

    direct = user_friends[user_id]
    suggestions = {}

    for f in direct:
        for mutual in user_friends.get(f, []):
            if mutual != user_id and mutual not in direct:
                suggestions[mutual] = suggestions.get(mutual, 0) + 1

    return sorted(suggestions.items(), key=lambda x: x[1], reverse=True)

def find_pages_you_might_like(user_id, data):
    user_pages = {u["id"]: set(u["liked_pages"]) for u in data["users"]}
    if user_id not in user_pages:
        return []

    liked = user_pages[user_id]
    suggestions = {}

    for other, pages in user_pages.items():
        if other != user_id:
            shared = liked.intersection(pages)
            for p in pages:
                if p not in liked:
                    suggestions[p] = suggestions.get(p, 0) + len(shared)

    return sorted(suggestions.items(), key=lambda x: x[1], reverse=True)
