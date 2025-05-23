from time import sleep
from datetime import datetime, timezone
from timekeeper import Timekeeper

def format_output(data):
    """Format the output data for better readability."""
    output = []
    output.append(f"Earth Time: {data['earth_time']}")
    output.append(f"Date: {data['date']}")
    output.append(f"Year: {data['year']}")
    output.append(f"Day of Year: {data['day_of_year']}")
    output.append(f"Week: {data['week']}")
    output.append(f"Season: {data['season']}")
    output.append(f"Month (Tribe): {data['month']}")
    output.append(f"Season Transition: {data['season_transition']}")
    output.append(f"Countdown to Next Season: {data['countdown_to_next_season']['days_left']} days until {data['countdown_to_next_season']['next_season']}")
    output.append(f"Priestly Order: Week {data['priestly_order']['week_number']} - {data['priestly_order']['order_name']}")
    output.append("Part of Day:")
    output.append(f"  Period: {data['part_of_day']['period']}")
    output.append(f"  Part: {data['part_of_day']['part']}")
    output.append(f"  Angel: {data['part_of_day']['angel']}")
    output.append(f"  Role: {data['part_of_day']['role']}")
    output.append(f"  Prayer: {data['part_of_day']['prayer']}")
    output.append("Celestial Gate:")
    celestial_gate = data['part_of_day']['celestial_gate']
    output.append(f"  Gate: {celestial_gate['gate']}")
    output.append(f"  Angel: {celestial_gate['angel']}")
    output.append(f"  Celestial Angle: {celestial_gate['celestial_angle']}")
    output.append(f"  Element: {celestial_gate['element']}")
    output.append(f"  Zodiac Sign: {celestial_gate['zodiac_sign']}")
    output.append(f"  Enochian Direction: {celestial_gate['enochian_direction']}")
    output.append(f"  Gate Name: {celestial_gate['gate_name']}")
    return "\n".join(output)

def main():
    """Continuously fetch and display real-time data."""
    print("Starting real-time celestial and angelic data display...")
    while True:
        try:
            # Create a Timekeeper instance with the current UTC time
            tk = Timekeeper(current_date=datetime.now(timezone.utc))
            
            # Fetch the current part of the day or night with celestial and angelic data
            data = tk.get_time_data()
            
            # Format and display the data
            formatted_output = format_output(data)
            print("\n" + "=" * 50)
            print(formatted_output)
            print("=" * 50 + "\n")
            
            # Wait for 60 seconds before updating
            sleep(60)
        except KeyboardInterrupt:
            print("\nExiting real-time display.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    main()