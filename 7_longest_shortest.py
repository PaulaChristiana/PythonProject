"""7. Calculate the longest and shortest successful run times across all types of apps (Frontend, Backend, API). 
Provide the timestamps for these occurrences"""

# from datetime import datetime

# def longest_shortest_run_times(file_to_read):
#     with open(file_to_read, 'r') as file:
#         log_data = file.readlines()

#     # Initialize variables to store the longest and shortest run times and their timestamps
#     longest_time = 0
#     shortest_time = float('inf')  # Set to infinity for initialization
#     longest_timestamp = ""
#     shortest_timestamp = ""

#     for line in log_data:
#         # Check if the line indicates a successful run and is not for the SYSTEM app
#         if 'has ran successfully' in line and 'SYSTEM' not in line:
#             parts = line.split()
#             app_name = parts[4]
#             run_time = int(parts[-2].replace('ms', ''))
#             timestamp = parts[0]

#             # Update the longest and shortest run times and their timestamps
#             if run_time > longest_time:
#                 longest_time = run_time
#                 longest_timestamp = timestamp
#             if run_time < shortest_time:
#                 shortest_time = run_time
#                 shortest_timestamp = timestamp

#     return (longest_timestamp, longest_time), (shortest_timestamp, shortest_time)

# # Replace with your actual file path
# longest_run = longest_shortest_run_times("output.txt")
# shortest_run = longest_shortest_run_times("output.txt")
# print(f"Longest run: {longest_run[0]} at {longest_run[1]}ms")
# print(f"Shortest run: {shortest_run[0]} at {shortest_run[1]}ms")

# def longest_shortest_run_times(file_to_read):
#     with open(file_to_read, 'r') as file:
#         log_data = file.readlines()

#     longest_time = 0
#     shortest_time = float('inf')
#     longest_timestamp = ""
#     shortest_timestamp = ""

#     for line in log_data:
#         if 'has ran successfully' in line and 'SYSTEM' not in line:
#             # Extracting timestamp, app name, and run time
#             try:
#                 parts = line.split()
#                 timestamp = parts[0]
#                 run_time_str = parts[-2]
#                 run_time = int(run_time_str.replace('ms', ''))  # Remove 'ms' and convert to integer

#                 # Update the longest and shortest run times and their timestamps
#                 if run_time > longest_time:
#                     longest_time = run_time
#                     longest_timestamp = timestamp
#                 if run_time < shortest_time:
#                     shortest_time = run_time
#                     shortest_timestamp = timestamp
#             except ValueError:
#                 print(f"Error processing line: {line}")

#     return (longest_timestamp, longest_time), (shortest_timestamp, shortest_time)

# # Replace with your actual file path
# longest_run, shortest_run = longest_shortest_run_times("output.txt")
# print(f"Longest run: {longest_run[0]} at {longest_run[1]}ms")
# print(f"Shortest run: {shortest_run[0]} at {shortest_run[1]}ms")

# def longest_shortest_run_times(file_to_read):
#     with open(file_to_read, 'r') as file:
#         log_data = file.readlines()

#     longest_time = 0
#     shortest_time = float('inf')
#     longest_timestamp = None
#     shortest_timestamp = None

#     for line in log_data:
#         if 'has ran successfully' in line and 'SYSTEM' not in line:
#             try:
#                 # Assuming the format is like "HH:MM:SS - [INFO] - AppName has ran successfully in XXms"
#                 parts = line.split()
#                 timestamp = parts[0]
#                 run_time_str = [s for s in parts if "ms" in s][0]  # Find the part with "ms"
#                 run_time = int(run_time_str.replace('ms', ''))

#                 if run_time > longest_time:
#                     longest_time = run_time
#                     longest_timestamp = timestamp

#                 if run_time < shortest_time:
#                     shortest_time = run_time
#                     shortest_timestamp = timestamp

#             except (ValueError, IndexError) as e:
#                 print(f"Error processing line: {line}\nError: {e}")

#     return (longest_timestamp, longest_time), (shortest_timestamp, shortest_time)

# # Replace with your actual file path
# longest_run, shortest_run = longest_shortest_run_times("output.txt")
# print(f"Longest run: {longest_run[0]} at {longest_run[1]}ms")
# print(f"Shortest run: {shortest_run[0]} at {shortest_run[1]}ms")

def run_times_per_app(file_to_read):
    with open(file_to_read, 'r') as file:
        log_data = file.readlines()

    # Dictionaries to store the longest and shortest run times for each app
    longest_runs = {}
    shortest_runs = {}

    for line in log_data:
        if 'has ran successfully' in line and 'SYSTEM' not in line:
            try:
                parts = line.split()
                timestamp = parts[0]
                app_name = parts[4]
                run_time_str = [s for s in parts if "ms" in s][0]
                run_time = int(run_time_str.replace('ms', ''))

                # Initialize if first occurrence of the app
                if app_name not in longest_runs:
                    longest_runs[app_name] = (timestamp, run_time)
                    shortest_runs[app_name] = (timestamp, run_time)

                # Update longest run
                if run_time > longest_runs[app_name][1]:
                    longest_runs[app_name] = (timestamp, run_time)

                # Update shortest run
                if run_time < shortest_runs[app_name][1]:
                    shortest_runs[app_name] = (timestamp, run_time)

            except (ValueError, IndexError) as e:
                print(f"Error processing line: {line}\nError: {e}")

    return longest_runs, shortest_runs

# Replace with your actual file path
longest_runs, shortest_runs = run_times_per_app("output.txt")

# Print results
print("Longest Runs per App:")
for app, (timestamp, run_time) in longest_runs.items():
    print(f"{app}: {timestamp} at {run_time}ms")

print("\nShortest Runs per App:")
for app, (timestamp, run_time) in shortest_runs.items():
    print(f"{app}: {timestamp} at {run_time}ms")
