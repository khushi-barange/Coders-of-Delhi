def display_summary(data):
    print("\n===== Dataset Summary =====")
    print(f"Total Users : {len(data['users'])}")
    print(f"Total Pages : {len(data['pages'])}")

    print("\nSample Users:")
    for u in data["users"][:5]:
        print(f"- {u['name']} (ID: {u['id']}), Friends: {len(u['friends'])}, Liked Pages: {len(u['liked_pages'])}")

    print("\nSample Pages:")
    for p in data["pages"][:5]:
        print(f"- {p['id']}: {p['name']}")
