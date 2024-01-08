# 6. Which third of day (00:00:00 - 07:59:59/08:00:00-15:59:59/16:00:00-23:59:59) had the most failed runs





from datetime import datetime

def third_of_day_with_most_failures(file_to_read):
    with open(file_to_read, 'r') as file:
        log_data = file.readlines()

    first_third, second_third, third_third = 0, 0, 0

    for line in log_data:
        if '[ERROR]' in line:
            try:
                time_str = line.split(' - ')[0]
                time_obj = datetime.strptime(time_str, "%H:%M:%S")

                if time_obj.hour < 8:
                    first_third += 1
                elif time_obj.hour < 16:
                    second_third += 1
                else:
                    third_third += 1
            except Exception as e:
                print(f"Error processing line: {line}\nError: {e}")

    most_failures = max(first_third, second_third, third_third)
    if most_failures == first_third:
        return "00:00:00 - 07:59:59", most_failures
    elif most_failures == second_third:
        return "08:00:00 - 15:59:59", most_failures
    else:
        return "16:00:00 - 23:59:59", most_failures

# Example usage
time_period, failures = third_of_day_with_most_failures("output.txt")
print(f"Time period with most failures: {time_period}, Failures: {failures}")
