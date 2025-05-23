from datetime import datetime, timezone, timedelta
from astral import LocationInfo
from astral.sun import sun
import heavenly_calendar as calendar        # renamed module
import priestly_orders  # your priestly_orders.py
import angelic_parts  # your angelic_parts.py
from celestial_correspondences import CELESTIAL_GATES  # New celestial gates module

# Define the names of the 12 tribes of Israel
TRIBES_OF_ISRAEL = [
    "Reuben", "Simeon", "Levi", "Judah", "Dan", "Naphtali",
    "Gad", "Asher", "Issachar", "Zebulun", "Joseph", "Benjamin"
]

class Timekeeper:
    def __init__(self, current_date=None, location=None):
        self.current_date = current_date or datetime.now(timezone.utc)
        self.location = location or LocationInfo("New York", "USA", "America/New_York", 40.7128, -74.0060)

    def get_sun_times(self):
        """Calculate sunrise and sunset times for the current date and location."""
        sun_times = sun(self.location.observer, date=self.current_date)
        return sun_times["sunrise"], sun_times["sunset"]

    def get_enochian_part_of_day_with_angel(self):
        """Calculate the current part of the day or night based on 18 parts."""
        sunrise, sunset = self.get_sun_times()

        if self.current_date < sunrise or self.current_date >= sunset:
            # Nighttime: from sunset to the next day's sunrise
            next_sunrise = sun(self.location.observer, date=self.current_date + timedelta(days=1))["sunrise"]
            total_night_minutes = (next_sunrise - sunset).total_seconds() / 60
            part_duration = total_night_minutes / 9  # 9 parts for night
            minutes_since_sunset = (self.current_date - sunset).total_seconds() / 60
            part_index = int(minutes_since_sunset // part_duration) + 1
            if part_index > len(angelic_parts.night_parts):
                raise IndexError("Part index out of range for night_parts.")
            part_info = angelic_parts.night_parts[part_index - 1]
            celestial_gate = self.get_celestial_gate(part_index)
            return {
                "period": "Night",
                "part": part_index,
                "angel": part_info["angel"],
                "role": part_info["role"],
                "prayer": part_info["prayer"],
                "celestial_gate": celestial_gate
            }
        else:
            # Daytime: from sunrise to sunset
            total_day_minutes = (sunset - sunrise).total_seconds() / 60
            part_duration = total_day_minutes / 9  # 9 parts for day
            minutes_since_sunrise = (self.current_date - sunrise).total_seconds() / 60
            part_index = int(minutes_since_sunrise // part_duration) + 1
            if part_index > len(angelic_parts.day_parts):
                raise IndexError("Part index out of range for day_parts.")
            part_info = angelic_parts.day_parts[part_index - 1]
            celestial_gate = self.get_celestial_gate(part_index)
            return {
                "period": "Day",
                "part": part_index,
                "angel": part_info["angel"],
                "role": part_info["role"],
                "prayer": part_info["prayer"],
                "celestial_gate": celestial_gate
            }

    def get_celestial_gate(self, part_index):
        """Retrieve celestial gate information based on the current part index."""
        if 1 <= part_index <= len(CELESTIAL_GATES):
            return CELESTIAL_GATES[part_index - 1]
        raise ValueError(f"Invalid part index {part_index}. Must be between 1 and 18.")

    def get_time_data(self):
        enochian_date = calendar.get_enochian_date(self.current_date)
        year = enochian_date["year"]
        day_of_year = enochian_date["day_of_year"]
        week = enochian_date["week"]
        season = calendar.get_season(day_of_year)
        
        # Determine the month (tribe) based on the day of the year
        month_index = (day_of_year - 1) // 30  # Assuming 30 days per month
        month_name = TRIBES_OF_ISRAEL[month_index % len(TRIBES_OF_ISRAEL)]
        
        # Check if today is a season transition
        print(f"Day of Year: {day_of_year}")
        is_transition = calendar.is_season_transition(day_of_year)
        print(f"Is Season Transition: {is_transition}")
        
        # Get countdown to the next season transition
        countdown = calendar.days_until_next_season_transition(day_of_year)
        print(f"Countdown to next season transition: {countdown}")
        
        # Use priestly_orders with current date for accurate calculation
        priestly = priestly_orders.get_current_priestly_order(self.current_date)

        part_of_day_info = self.get_enochian_part_of_day_with_angel()

        return {
            "earth_time": self.current_date.strftime("%Y-%m-%d %H:%M:%S %Z"),
            "date": self.current_date.strftime("%Y-%m-%d"),
            "year": year,
            "day_of_year": day_of_year,
            "week": week,
            "season": season,
            "month": month_name,  # Tribe name as the month
            "season_transition": is_transition,
            "countdown_to_next_season": countdown,
            "priestly_order": priestly,
            "part_of_day": part_of_day_info,
        }

if __name__ == "__main__":
    tk = Timekeeper()
    data = tk.get_time_data()
    for key, value in data.items():
        if isinstance(value, dict):
            print(f"{key}:")
            for k2, v2 in value.items():
                print(f"  {k2}: {v2}")
        else:
            print(f"{key}: {value}")