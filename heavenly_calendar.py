from datetime import datetime, timedelta, timezone

# Epoch starting point: Year 0 (Creation), set to a known date with UTC timezone
# Adjust this date to match your creation baseline
CREATION_DATE = datetime(1, 1, 1, tzinfo=timezone.utc)  # now timezone-aware

# Constants
DAYS_IN_YEAR_364 = 364
DAYS_IN_YEAR_360 = 360
DAYS_IN_WEEK = 7

# Define the names of the 12 tribes of Israel
TRIBES_OF_ISRAEL = [
    "Reuben", "Simeon", "Levi", "Judah", "Dan", "Naphtali",
    "Gad", "Asher", "Issachar", "Zebulun", "Joseph", "Benjamin"
]

def get_days_since_creation(current_date=None):
    """Returns total days since creation."""
    if not current_date:
        current_date = datetime.now(timezone.utc)  # timezone-aware current date
    # Both current_date and CREATION_DATE are timezone-aware now
    return (current_date - CREATION_DATE).days

def get_tribe_for_month(day_of_year):
    """Return the tribe name corresponding to the current month."""
    month_index = (day_of_year - 1) // 30  # Assuming 30 days per month
    return TRIBES_OF_ISRAEL[month_index % len(TRIBES_OF_ISRAEL)]

def get_enochian_date(current_date=None, calendar_type="364"):
    """Returns current year, day of year, week, and tribe (based on 364 or 360-day calendar)."""
    days_since_creation = get_days_since_creation(current_date)

    if calendar_type == "360":
        year = days_since_creation // DAYS_IN_YEAR_360
        day_of_year = days_since_creation % DAYS_IN_YEAR_360 + 1
    else:  # Default to 364-day Enochian calendar
        year = days_since_creation // DAYS_IN_YEAR_364
        day_of_year = days_since_creation % DAYS_IN_YEAR_364 + 1

    week = (day_of_year - 1) // DAYS_IN_WEEK + 1
    tribe = get_tribe_for_month(day_of_year)

    return {
        "year": year,
        "day_of_year": day_of_year,
        "week": week,
        "tribe": tribe
    }

def is_season_transition(day_of_year):
    """Check if today marks a season change (based on Enoch's 364-day calendar)."""
    return day_of_year in [1, 92, 183, 274]

def days_until_next_season_transition(day_of_year):
    """Calculate how many days are left until the next season transition and return a countdown."""
    # List of season transition days and their corresponding seasons
    season_transitions = [
        (1, "Spring"),
        (92, "Summer"),
        (183, "Autumn"),
        (274, "Winter")
    ]
    
    # Find the next transition day and season
    for transition_day, season_name in season_transitions:
        if day_of_year < transition_day:
            days_left = transition_day - day_of_year
            return {
                "days_left": days_left,
                "next_season": season_name
            }
    
    # If no future transition is found, wrap around to the next year's first transition
    days_left = 364 - day_of_year + 1
    return {
        "days_left": days_left,
        "next_season": "Spring"
    }

def get_season(day_of_year):
    """Return season name based on Enoch 364-day year."""
    if 1 <= day_of_year <= 91:
        return "Spring"
    elif 92 <= day_of_year <= 182:
        return "Summer"
    elif 183 <= day_of_year <= 273:
        return "Autumn"
    else:
        return "Winter"

def get_month_and_tribe(day_of_year):
    """Return the month (tribe) and its index based on the day of the year."""
    month_index = (day_of_year - 1) // 30  # Assuming 30 days per month
    tribe = TRIBES_OF_ISRAEL[month_index % len(TRIBES_OF_ISRAEL)]
    return {
        "month_index": month_index + 1,  # 1-based index for months
        "tribe": tribe
    }