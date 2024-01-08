# 3. How many times each app (Frontend, Backend, API, System) failed throughout the day

def count_logs(file_to_read):
    # Open the file and read its contents
    with open(file_to_read, mode="r") as file:
        log_data = file.readlines()

    # Initialize counters for each log type and app
    info_count = {}
    debug_count = {}
    error_count = {}

    # Process each line in the file
    for line in log_data:
        # Check if the line contains 'INFO', 'DEBUG', or 'ERROR'
        if '[INFO]' in line:
            # Extract the app name and update its count
            app_name = line.split('-')[1].strip().split()[0]
            info_count[app_name] = info_count.get(app_name, 0) + 0.5
        elif '[DEBUG]' in line:
            app_name = line.split('-')[1].strip().split()[0]
            debug_count[app_name] = debug_count.get(app_name, 0) + 1
        elif '[ERROR]' in line:
            app_name = line.split('-')[1].strip().split()[0]
            error_count[app_name] = error_count.get(app_name, 0) + 1

    # Prepare the final output string
    output_str = ""
    for app in set(info_count.keys()).union(debug_count.keys(), error_count.keys()):
        output_str += f"{app} - INFO logs: {int(info_count.get(app, 0))}\n"
        output_str += f"{app} - DEBUG logs: {debug_count.get(app, 0)}\n"
        output_str += f"{app} - ERROR logs: {error_count.get(app, 0)}\n"

    return output_str.strip()

# Example usage
log_counts_str = count_logs("output.txt")
print(log_counts_str)


# nu indica cum trebuie