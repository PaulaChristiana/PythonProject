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

    return failure_counts