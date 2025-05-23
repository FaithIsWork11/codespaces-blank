from datetime import datetime, timezone

# 24 Priestly Orders from 1 Chronicles 24
PRIESTLY_ORDERS = [
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
    """
    Calculate the current priestly order based on the number of weeks since creation.

    Args:
        current_date (datetime, optional): The current date in UTC. Defaults to now.

    Returns:
        dict: A dictionary containing the current week number and the priestly order name.
    """
    if current_date is None:
        current_date = datetime.now(timezone.utc)  # Use current UTC time if not provided
    
    # Calculate the number of full weeks since the creation start date
    delta = current_date - CREATION_START
    total_weeks = delta.days // 7
    
    # Determine the current priestly order
    index = total_weeks % len(PRIESTLY_ORDERS)
    return {
        "week_number": total_weeks + 1,  # Add 1 to make it 1-based
        "order_name": PRIESTLY_ORDERS[index],
    }

# Example usage
if __name__ == "__main__":
    current = get_current_priestly_order()
    print(f"Week {current['week_number']}: {current['order_name']}")