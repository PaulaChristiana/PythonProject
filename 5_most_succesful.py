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

#final impresion
most_successful_app, most_successes = app_with_most_successful_runs("output.txt")
print(f"App with the most successful runs: {most_successful_app} ({most_successes} successful runs)")