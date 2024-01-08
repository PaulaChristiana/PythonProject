# # # def average_run_time(file_to_read):
# # #     # Open the file and read its contents
# # #     with open(file_to_read, mode="r") as file:
# # #         log_data = file.readlines()

# # #     # Initialize dictionaries to store total run times and counts
# # #     total_run_time = {'FrontendApp': 0, 'BackendApp': 0, 'API': 0}
# # #     run_counts = {'FrontendApp': 0, 'BackendApp': 0, 'API': 0}

# # #     # Process each line in the file
# # #     for line in log_data:
# # #         if 'has ran successfully' in line:
# # #             # Extract app name and run time
# # #             parts = line.split('-')
# # #             app_name = parts[1].strip().split()[0]
# # #             run_time = int(parts[2].strip().split()[0])

# # #             # Update total run time and count for the app
# # #             if app_name in total_run_time:
# # #                 total_run_time[app_name] += run_time
# # #                 run_counts[app_name] += 1

# # #     # Prepare the final output string
# # #     output_str = ""
# # #     for app in total_run_time:
# # #         if run_counts[app] > 0:
# # #             average_time = total_run_time[app] / run_counts[app]
# # #             output_str += f"{app} - Average Successful Run Time: {average_time:.2f}ms\n"
# # #         else:
# # #             output_str += f"{app} - No successful runs\n"

# # #     return output_str.strip()

# # # # Example usage
# # # average_run_time_str = average_run_time("test.txt")
# # # print(average_run_time_str)


# # def average_run_time(file_to_read):
# #     with open(file_to_read, mode="r") as file:
# #         log_data = file.readlines()

# #     total_run_time = {'FrontendApp': 0, 'BackendApp': 0, 'API': 0}
# #     run_counts = {'FrontendApp': 0, 'BackendApp': 0, 'API': 0}

# #     for line in log_data:
# #         if 'has ran successfully' in line:
# #             parts = line.split()
# #             app_name = parts[4]  # Assuming the app name is always the fifth word
# #             try:
# #                 # Extract run time (assuming it's always right before 'ms')
# #                 run_time = int(parts[-2].replace('ms', ''))
                
# #                 if app_name in total_run_time:
# #                     total_run_time[app_name] += run_time
# #                     run_counts[app_name] += 1
# #             except ValueError:
# #                 # Handle the case where run time is not correctly formatted
# #                 print(f"Error processing line: {line}")

# #     output_str = ""
# #     for app in total_run_time:
# #         if run_counts[app] > 0:
# #             average_time = total_run_time[app] / run_counts[app]
# #             output_str += f"{app} - Average Successful Run Time: {average_time:.2f}ms\n"
# #         else:
# #             output_str += f"{app} - No successful runs\n"

# #     return output_str.strip()

# # # Replace with your actual file path
# # average_run_time_str = average_run_time("test.txt")
# # print(average_run_time_str)


# # def average_run_time(file_to_read):
# #     with open(file_to_read, mode="r") as file:
# #         log_data = file.readlines()

# #     total_run_time = {'FrontendApp': 0, 'BackendApp': 0, 'API': 0}
# #     run_counts = {'FrontendApp': 0, 'BackendApp': 0, 'API': 0}

# #     for line in log_data:
# #         if 'has ran successfully' in line:
# #             parts = line.split()
# #             app_name = parts[4]  # Assuming the app name is always the fifth word

# #             # Skip if the app is 'SYSTEM'
# #             if app_name == 'SYSTEM':
# #                 continue

# #             try:
# #                 # Extract run time (assuming it's always right before 'ms')
# #                 run_time = int(parts[-2].replace('ms', ''))
                
# #                 if app_name in total_run_time:
# #                     total_run_time[app_name] += run_time
# #                     run_counts[app_name] += 1
# #             except ValueError:
# #                 # Handle the case where run time is not correctly formatted
# #                 print(f"Error processing line: {line}")

# #     output_str = ""
# #     for app in total_run_time:
# #         if run_counts[app] > 0:
# #             average_time = total_run_time[app] / run_counts[app]
# #             output_str += f"{app} - Average Successful Run Time: {average_time:.2f}ms\n"
# #         else:
# #             output_str += f"{app} - No successful runs\n"

# #     return output_str.strip()

# # # Replace with your actual file path
# # average_run_time_str = average_run_time("test.txt")
# # print(average_run_time_str)


# # def average_run_time(file_to_read):
# #     with open(file_to_read, mode="r") as file:
# #         log_data = file.readlines()

# #     # Dictionaries to store total run times and counts for each app
# #     total_run_time = {}
# #     run_counts = {}

# #     for line in log_data:
# #         if 'has ran successfully' in line:
# #             parts = line.split()
# #             app_name = parts[4]  # Assuming the app name is always the fifth word
# #             try:
# #                 # Extract run time (assuming it's right before 'ms')
# #                 run_time = int(parts[-2].replace('ms', ''))

# #                 # Update total run time and count for this app
# #                 if app_name not in total_run_time:
# #                     total_run_time[app_name] = 0
# #                     run_counts[app_name] = 0
# #                 total_run_time[app_name] += run_time
# #                 run_counts[app_name] += 1
# #             except ValueError:
# #                 # pass
# #                 # Handle cases where run time is not correctly formatted
# #                 print(f"Error processing line: {line}")

# #     # String to store the final output
# #     output_str = ""
# #     for app in total_run_time:
# #         if run_counts[app] > 0:
# #             average_time = total_run_time[app] / run_counts[app]
# #             output_str += f"{app} - Average Successful Run Time: {average_time:.2f}ms\n"
# #         else:
# #             output_str += f"{app} - No successful runs\n"

# #     return output_str.strip()

# # # Replace with your actual file path
# # average_run_time_str = average_run_time("test.txt")
# # print(average_run_time_str)


# # def average_run_time(file_to_read):
# #     with open(file_to_read, mode="r") as file:
# #         log_data = file.readlines()

# #     total_run_time = {}
# #     run_counts = {}

# #     for line in log_data:
# #         if 'has ran successfully' in line:
# #             parts = line.split()
            
# #             # Extract the app name; it is expected after '[INFO]' and before 'has'
# #             app_index = parts.index('has') - 1
# #             app_name = parts[app_index]

# #             # Extract and convert the run time (expected before 'ms')
# #             run_time_index = parts.index('ms') - 1
# #             run_time = int(parts[run_time_index])

# #             # Update the run time and count for the app
# #             if app_name in total_run_time:
# #                 total_run_time[app_name] += run_time
# #                 run_counts[app_name] += 1
# #             else:
# #                 total_run_time[app_name] = run_time
# #                 run_counts[app_name] = 1

# #     # Prepare and return the output string
# #     output_str = ""
# #     for app in total_run_time:
# #         average_time = total_run_time[app] / run_counts[app]
# #         output_str += f"{app} - Average Successful Run Time: {average_time:.2f}ms\n"

# #     return output_str.strip()

# # # Example usage
# # average_run_time_str = average_run_time("test.txt")
# # print(average_run_time_str)

# import re

# def average_run_time(file_to_read):
#     with open(file_to_read, mode="r") as file:
#         log_data = file.readlines()

#     total_run_time = {}
#     run_counts = {}

#     for line in log_data:
#         if 'has ran successfully' in line:
#             # Using regex to find the app name and run time
#             match = re.search(r"\[INFO\] - (\w+) has ran successfully in (\d+)ms", line)
#             if match:
#                 app_name = match.group(1)
#                 run_time = int(match.group(2))

#                 # Update the run time and count for the app
#                 if app_name in total_run_time:
#                     total_run_time[app_name] += run_time
#                     run_counts[app_name] += 1
#                 else:
#                     total_run_time[app_name] = run_time
#                     run_counts[app_name] = 1

#     # Prepare and return the output string
#     output_str = ""
#     for app in total_run_time:
#         average_time = total_run_time[app] / run_counts[app]
#         output_str += f"{app} - Average Successful Run Time: {average_time:.2f}ms\n"

#     return output_str.strip()

# # Example usage
# average_run_time_str = average_run_time("test.txt")
# print(average_run_time_str)

import re

# def average_run_time_excluding_system(file_to_read):
#     with open(file_to_read, mode="r") as file:
#         log_data = file.readlines()

#     total_run_time = {}
#     run_counts = {}

#     for line in log_data:
#         if 'has ran successfully' in line:
#             # Using regex to find the app name and run time
#             match = re.search(r"\[INFO\] - (\w+) has ran successfully in (\d+)ms", line)
#             if match:
#                 app_name = match.group(1)
#                 run_time = int(match.group(2))

#                 # Skip if the app is 'SYSTEM'
#                 if app_name == 'SYSTEM':
#                     continue

#                 # Update the run time and count for the app
#                 if app_name in total_run_time:
#                     total_run_time[app_name] += run_time
#                     run_counts[app_name] += 1
#                 else:
#                     total_run_time[app_name] = run_time
#                     run_counts[app_name] = 1

#     # Prepare and return the output string
#     output_str = ""
#     for app in total_run_time:
#         average_time = total_run_time[app] / run_counts[app]
#         output_str += f"{app} - Average Successful Run Time: {average_time:.2f}ms\n"

#     return output_str.strip()

# # Example usage
# average_run_time_str = average_run_time_excluding_system("test.txt")
# print(average_run_time_str)

# def average_run_time_excluding_system(file_to_read):
#     with open(file_to_read, 'r') as file:
#         log_data = file.readlines()

#     total_run_time = {}
#     run_counts = {}

#     for line in log_data:
#         # Check if the line indicates a successful run
#         if 'has ran successfully' in line:
#             # Split the line into words
#             words = line.split()

#             # Find the app name and run time
#             app_name = words[4]  # Assuming the app name is the fifth word
#             run_time_str = words[-2]  # Assuming the run time is the second last word
#             run_time_ms = run_time_str.replace('ms', '')  # Remove 'ms' to get the number

#             # Skip if the app is SYSTEM
#             if app_name == 'SYSTEM':
#                 continue

#             # Convert run time to an integer
#             try:
#                 run_time = int(run_time_ms)
#             except ValueError:
#                 print(f"Error processing line: {line}")
#                 continue

#             # Update the total run time and count for each app
#             if app_name in total_run_time:
#                 total_run_time[app_name] += run_time
#                 run_counts[app_name] += 1
#             else:
#                 total_run_time[app_name] = run_time
#                 run_counts[app_name] = 1

#     # Prepare the final output string
#     output_str = ""
#     for app in total_run_time:
#         average_time = total_run_time[app] / run_counts[app]
#         output_str += f"{app} - Average Successful Run Time: {average_time:.2f}ms\n"

#     return output_str

# # Example usage
# average_run_time_str = average_run_time_excluding_system("test.txt")
# print(average_run_time_str)


# def average_run_time_excluding_system(file_to_read):
#     # Open the file
#     with open(file_to_read, 'r') as file:
#         log_data = file.readlines()

#     # Initialize dictionaries to store total run times and counts
#     total_run_time = {}
#     run_counts = {}

#     # Go through each line in the file
#     for line in log_data:
#         # Check if the line indicates a successful run
#         if 'has ran successfully' in line:
#             # Split the line into words
#             words = line.split()

#             # Extract the app name (assuming it's the 5th word in the line)
#             app_name = words[4]

#             # Skip if the app is SYSTEM
#             if app_name == 'SYSTEM':
#                 continue

#             # Extract the run time (assuming it's right before 'ms')
#             run_time_str = words[-2]  # Get the second last word
#             run_time = int(run_time_str.replace('ms', ''))  # Remove 'ms' and convert to integer

#             # Update total run time and count for the app
#             if app_name not in total_run_time:
#                 total_run_time[app_name] = 0
#                 run_counts[app_name] = 0
#             total_run_time[app_name] += run_time
#             run_counts[app_name] += 1

#     # Compute and print the average run time for each app
#     for app in total_run_time:
#         average_time = total_run_time[app] / run_counts[app]
#         print(f"{app} - Average Successful Run Time: {average_time:.2f}ms")

# # Call the function with the file path
# average_run_time_excluding_system("test.txt")


# def average_run_time_excluding_system(file_to_read):
#     # Open the file
#     with open(file_to_read, 'r') as file:
#         log_data = file.readlines()

#     # Initialize dictionaries to store total run times and counts
#     total_run_time = {}
#     run_counts = {}

#     # Go through each line in the file
#     for line in log_data:
#         # Check if the line indicates a successful run
#         if 'has ran successfully' in line:
#             # Find the app name and run time using string manipulation
#             parts = line.split(' - ')
#             app_name = parts[1].split()[0]

#             # Skip if the app is SYSTEM
#             if app_name == 'SYSTEM':
#                 continue

#             # Find the run time
#             run_time_str = parts[2].split()[0]
#             run_time = int(run_time_str)

#             # Update total run time and count for the app
#             if app_name not in total_run_time:
#                 total_run_time[app_name] = 0
#                 run_counts[app_name] = 0
#             total_run_time[app_name] += run_time
#             run_counts[app_name] += 1

#     # Compute and print the average run time for each app
#     for app in total_run_time:
#         average_time = total_run_time[app] / run_counts[app]
#         print(f"{app} - Average Successful Run Time: {average_time:.2f}ms")

# # Call the function with the file path
# average_run_time_excluding_system("test.txt")

import re

def average_run_time_excluding_system(file_to_read):
    with open(file_to_read, 'r') as file:
        log_data = file.readlines()

    total_run_time = {}
    run_counts = {}

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
        print(f"{app} - Average Successful Run Time: {average_time:.2f}ms")


average_run_time_excluding_system("test.txt")
