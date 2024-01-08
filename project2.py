

import re

def average_run_time_excluding_system(file_to_read):
    with open(file_to_read, 'r') as file:
        log_data = file.readlines()

    total_run_time = {}
    run_counts = {}
    app_avg= {}

    for line in log_data:
        # Check if the line indicates a successful run
        if 'has ran successfully' in line:
            # Use regular expression to find the app name and run time
            match = re.search(r'(\w+) has ran successfully in (\d+)ms', line)
            if match:
                app_name = match.group(1)
                run_time = int(match.group(2))

                # Skip if the app is SYSTEM
                if app_name == 'SYSTEM':
                    continue

                # Update the total run time and count
                if app_name not in total_run_time:
                    total_run_time[app_name] = 0
                    run_counts[app_name] = 0
                total_run_time[app_name] += run_time
                run_counts[app_name] += 1

    # Calculate and print the average run time for each app
    for app in total_run_time:
        average_time = total_run_time[app] / run_counts[app]
        app_avg[app]=round(average_time,2)
        print(f"{app} - Average Successful Run Time: {average_time:.2f}ms")
    return app_avg


print(average_run_time_excluding_system("test2.txt"))
