"""8 Identify the hour of the day (eg., 00:00:00-00:59:00, 01:00:00-01:59:00 etc.) when each app type (Frontend, Backend, API) 
had the most activities (INFO/ERROR/DEBUG)"""

from collections import defaultdict
import re

def busiest_hour_per_app(file_to_read):
    with open(file_to_read, 'r') as file:
        log_data = file.readlines()

    # Dictionary to store activity counts per hour for each app
    activities_per_hour = defaultdict(lambda: defaultdict(int))

    for line in log_data:
        # Exclude SYSTEM logs
        if 'SYSTEM' not in line:
            # Extract hour and app name
            match = re.search(r'(\d{2}):\d{2}:\d{2} - \[\w+\] - (\w+)', line)
            if match:
                hour, app_name = match.groups()
                # Increment the count for the hour for this app
                activities_per_hour[app_name][hour] += 1

    # Determine the busiest hour for each app
    busiest_hours = {}
    for app, hours in activities_per_hour.items():
        busiest_hour = max(hours, key=hours.get)
        busiest_hours[app] = (busiest_hour, hours[busiest_hour])

    return busiest_hours

# file
busiest_hours = busiest_hour_per_app("test2.txt")
busiest_hours

busiest_hours_str = "Busiest Hours for Each App:\n"
for app, (hour, count) in busiest_hours.items():
    busiest_hours_str += f"{app}: Busiest hour was between {hour}:00:00 and {hour}:59:59 with {count} activities.\n"

print(busiest_hours_str)

