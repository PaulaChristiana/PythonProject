"""7. Calculate the longest and shortest successful run times across all types of apps (Frontend, Backend, API). 
Provide the timestamps for these occurrences"""



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

# file 
longest_runs, shortest_runs = run_times_per_app("output.txt")

# Print results
print("Longest Runs per App:")
for app, (timestamp, run_time) in longest_runs.items():
    print(f"{app}: {timestamp} at {run_time}ms")

print("\nShortest Runs per App:")
for app, (timestamp, run_time) in shortest_runs.items():
    print(f"{app}: {timestamp} at {run_time}ms")
