from datetime import datetime, timedelta, timezone

# Epoch starting point: Year 0 (Creation), set to a known date with UTC timezone
# Adjust this date to match your creation baseline
CREATION_DATE = datetime(1, 1, 1, tzinfo=timezone.utc)  # now timezone-aware

# Constants
DAYS_IN_YEAR_364 = 364
DAYS_IN_YEAR_360 = 360
DAYS_IN_WEEK = 7

def get_days_since_creation(current_date=None):
    """Returns total days since creation."""
    if not current_date:
        current_date = datetime.now(timezone.utc)  # timezone-aware current date
    # Both current_date and CREATION_DATE are timezone-aware now
    return (current_date - CREATION_DATE).days

def get_enochian_date(current_date=None, calendar_type="364"):
    """Returns current year, day of year, and week (based on 364 or 360-day calendar)."""
    days_since_creation = get_days_since_creation(current_date)

    if calendar_type == "360":
        year = days_since_creation // DAYS_IN_YEAR_360
        day_of_year = days_since_creation % DAYS_IN_YEAR_360 + 1
    else:  # Default to 364-day Enochian calendar
        year = days_since_creation // DAYS_IN_YEAR_364
        day_of_year = days_since_creation % DAYS_IN_YEAR_364 + 1

    week = (day_of_year - 1) // DAYS_IN_WEEK + 1

    return {
        "year": year,
        "day_of_year": day_of_year,
        "week": week
    }

def is_season_transition(day_of_year):
    """Check if today marks a season change (based on Enoch’s 364-day: every 91 days)."""
    return day_of_year in [1, 92, 183, 274]

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
