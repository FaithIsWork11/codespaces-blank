from datetime import datetime, timezone
import heavenly_calendar as calendar        # renamed module
import priestly_orders  # your priestly_orders.py
import angelic_parts  # your angelic_parts.py

class Timekeeper:
    def __init__(self, current_date=None):
        self.current_date = current_date or datetime.now(timezone.utc)

    def get_time_data(self):
        enochian_date = calendar.get_enochian_date(self.current_date)
        year = enochian_date["year"]
        day_of_year = enochian_date["day_of_year"]
        week = enochian_date["week"]
        season = calendar.get_season(day_of_year)
        
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
            "season_transition": is_transition,
            "countdown_to_next_season": countdown,
            "priestly_order": priestly,
            "part_of_day": part_of_day_info,
        }

    def get_enochian_part_of_day_with_angel(self):
        hour = self.current_date.hour
        minute = self.current_date.minute

        if 6 <= hour < 18:
            total_minutes = (hour - 6) * 60 + minute
            part_index = total_minutes // 80 + 1
            if part_index > len(angelic_parts.day_parts):
                raise IndexError("Part index out of range for day_parts.")
            part_info = angelic_parts.day_parts[part_index - 1]
            return {
                "period": "Day",
                "part": part_index,
                "angel": part_info["angel"],
                "role": part_info["role"],
                "prayer": part_info["prayer"],
            }
        else:
            if hour < 6:
                hour += 24
            total_minutes = (hour - 18) * 60 + minute
            part_index = total_minutes // 80 + 1
            if part_index > len(angelic_parts.night_parts):
                raise IndexError("Part index out of range for night_parts.")
            part_info = angelic_parts.night_parts[part_index - 1]
            return {
                "period": "Night",
                "part": part_index,
                "angel": part_info["angel"],
                "role": part_info["role"],
                "prayer": part_info["prayer"],
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