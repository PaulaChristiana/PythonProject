from collections import Counter
import re

def count(file_to_read):
    with open(file_to_read, mode="r") as file:
        log_data = file.read()
    
    # Corrected regular expression to capture both log type and app name
    log_entries = re.findall(r"\[([A-Z]+)\] - ([\w]+)", log_data)
    
    log_counts = Counter()
    for log_type, app in log_entries:
        if log_type == "INFO":
            log_counts[(log_type, app)] += 0.5
        else:
            log_counts[(log_type, app)] += 1
    
    # Formatting the output as a string
    output_str = ""
    for (log_type, app), count in log_counts.items():
        output_str += f"{app} - {log_type} logs: {int(count)}\n"

    return output_str.strip()

# Update the file name or path as necessary
log_counts_str = count("output.txt")
print(log_counts_str)
