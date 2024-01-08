# 3 How many times each app (Frontend, Backend, API, System) failed throughout the day

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

    # Print the failure count for each app
    for app, count in failure_counts.items():
        print(f"{app} failures: {count}")

# Replace with your actual file path
count_app_failures("test.txt")


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

    # Print the failure count for each app and the app with the most failures
    for app, count in failure_counts.items():
        print(f"{app} failures: {count}")
    print(f"\nApp with the most failures: {most_failed_app} ({most_failures} failures)")

# Replace with your actual file path
count_app_failures("test.txt")


# 5. App with the most succesful runs (INFO) and how many

def app_with_most_successful_runs(file_to_read):
    with open(file_to_read, 'r') as file:
        log_data = file.readlines()

    # Initialize a dictionary to store success counts for each app
    success_counts = {'FrontendApp': 0, 'BackendApp': 0, 'API': 0, 'SYSTEM': 0}

    for line in log_data:
        # Check if the line indicates a successful run
        if '[INFO]' in line and 'has ran successfully' in line:
            # Check for each app and increment the count
            if 'FrontendApp' in line:
                success_counts['FrontendApp'] += 1
            elif 'BackendApp' in line:
                success_counts['BackendApp'] += 1
            elif 'API' in line:
                success_counts['API'] += 1
            elif 'SYSTEM' in line:
                success_counts['SYSTEM'] += 1

    # Determine the app with the most successful runs
    most_successful_app = max(success_counts, key=success_counts.get)
    most_successes = success_counts[most_successful_app]

    return most_successful_app, most_successes

# Replace with your actual file path
most_successful_app, most_successes = app_with_most_successful_runs("test.txt")
print(f"App with the most successful runs: {most_successful_app} ({most_successes} successful runs)")
