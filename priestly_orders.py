from datetime import datetime, timezone

# 24 Priestly Orders from 1 Chronicles 24
priestly_orders = [
    "Jehoiarib", "Jedaiah", "Harim", "Seorim",
    "Malchijah", "Mijamin", "Hakkoz", "Abijah",
    "Jeshuah", "Shecaniah", "Eliashib", "Jakim",
    "Huppah", "Jeshebeab", "Bilgah", "Immer",
    "Hezir", "Aphses", "Pethahiah", "Jehezekel",
    "Jachin", "Gamul", "Delaiah", "Maaziah"
]

# Assume Year 0, Week 1 starts on a known date (UTC timezone-aware)
CREATION_START = datetime(2025, 1, 1, tzinfo=timezone.utc)  # timezone-aware

def get_current_priestly_order(current_date=None):
    if current_date is None:
        current_date = datetime.now(timezone.utc)  # timezone-aware
    
    # How many full weeks have passed since creation?
    delta = current_date - CREATION_START
    total_weeks = delta.days // 7
    
    # Get the current week's priestly course
    index = total_weeks % len(priestly_orders)
    return {
        "week_number": total_weeks + 1,
        "order_name": priestly_orders[index],
        }

# Example usage
if __name__ == "__main__":
    current = get_current_priestly_order()
    print(f"Week {current['week_number']}: {current['order_name']} ")
