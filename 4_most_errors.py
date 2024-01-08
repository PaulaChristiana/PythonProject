# 4. App with the most failed runs (ERROR) and how many
def count_app_failures(file_to_read):
    with open(file_to_read, 'r') as file:
        log_data = file.readlines()

    # Initialize a dictionary to store failure counts for each app
    failure_counts = {'FrontendApp': 0, 'BackendApp': 0, 'API': 0, 'SYSTEM': 0}

    for line in log_data:
        # Check if the line indicates a failure
        if '[ERROR]' in line:
            # Check for each app and increment the count
            if 'FrontendApp' in line:
                failure_counts['FrontendApp'] += 1
            elif 'BackendApp' in line:
                failure_counts['BackendApp'] += 1
            elif 'API' in line:
                failure_counts['API'] += 1
            elif 'SYSTEM' in line:
                failure_counts['SYSTEM'] += 1

    # Determine the app with the most failures
    most_failed_app = max(failure_counts, key=failure_counts.get)
    most_failures = failure_counts[most_failed_app]

    return most_failed_app, most_failures
    


most_failed_app, most_failures = count_app_failures("output.txt")

print(f"The app with the most failed runs: {most_failed_app} ({most_failures} failed runs)")