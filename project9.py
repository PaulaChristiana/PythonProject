from collections import defaultdict
import re


def calculate_failure_rates(file_to_read):
    with open(file_to_read, 'r') as file:
        log_data = file.readlines()

    # Dictionaries to store total and error log counts for each app
    total_logs = defaultdict(int)
    error_logs = defaultdict(int)

    for line in log_data:
        # Extract log type and app name
        match = re.search(r'\[\w+\] - (\w+)', line)
        if match:
            app_name = match.group(1)
            # Count each log for the app
            total_logs[app_name] += 1
            # Count only error logs for the app
            if '[ERROR]' in line:
                error_logs[app_name] += 1

    # Calculate and store failure rates for each app
    failure_rates = {}
    for app in total_logs:
        if total_logs[app] > 0:  # Prevent division by zero
            rate = (error_logs[app] / total_logs[app]) * 100
            failure_rates[app] = round(rate,2)
            
    return failure_rates

# Example usage with a hypothetical file path
failure_rates = calculate_failure_rates("test2.txt")

# Format the output as a string
failure_rates_str = "Failure Rates for Each App:\n"
for app, rate in failure_rates.items():
    failure_rates_str += f"{app}: {rate:.2f}% failure rate\n"

print(failure_rates_str)

