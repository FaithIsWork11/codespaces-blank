from calendar import get_enochian_date, get_season

date_info = get_enochian_date()
print(f"Year: {date_info['year']}, Day: {date_info['day_of_year']}, Week: {date_info['week']}")
print(f"Season: {get_season(date_info['day_of_year'])}")
