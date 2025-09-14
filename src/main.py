from src.data_loader import load_data, clean_data
from src.display import display_summary
from src.analysis import most_connected_user, most_popular_page
from src.recommendations import find_people_you_may_know, find_pages_you_might_like

if __name__ == "__main__":
    # Load and clean
    data = load_data("data/massive_data.json")
    data = clean_data(data)

    # Summary
    display_summary(data)

    # Insights
    user, friends = most_connected_user(data)
    print(f"\nMost Connected User: {user} ({friends} friends)")

    page, count = most_popular_page(data)
    print(f"Most Popular Page : {page} (liked by {count} users)")

    # Recommendations for a sample user
    user_id = 1  # Example: Amit
    print(f"\n--- Recommendations for User {user_id} ---")

    people = find_people_you_may_know(user_id, data)
    print("People You May Know:")
    for pid, score in people[:5]:
        name = next(u["name"] for u in data["users"] if u["id"] == pid)
        print(f"- {name} (ID {pid}), Mutual Friends: {score}")

    pages = find_pages_you_might_like(user_id, data)
    print("\nPages You Might Like:")
    for pgid, score in pages[:5]:
        name = next(p["name"] for p in data["pages"] if p["id"] == pgid)
        print(f"- {name} (ID {pgid}), Score: {score}")
