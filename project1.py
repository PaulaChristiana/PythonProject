"""1. How many INFO/DEBUG/ERROR logs per type of app (INFO 2 entries count as one log)"""


from collections import*
import re

def count(file_to_read):
    with open(file_to_read, mode = "r") as file:
        log_data = file.read()
        
    # log_entries = re.findall(r"\[([A-Z]+)\] - ([\w]+)", log_data)    
    log_entries = re.findall(r"\[([A-Z]+)\] - ([\w]+)", log_data) 
    
    log_counts = Counter()
    for log_type, app in log_entries:
        if log_type == "INFO":
            log_counts[(log_type, app)] += 0.5
        else:
            log_counts[(log_type,app)] += 1
    return log_counts
            
    #output_str = ""
    #for (log_type), count in log_counts.items():
     #   output_str += f"{0} - {log_type} logs: {int(count)}\n" 
    # return{k: int(v) for k, v in log_counts.items() if v >= 1}
    #return output_str.strip()
# log_counts = count("test.txt")
# print(log_counts)

#log_counts = count("test2.txt")
#print(log_counts)
#print(log_counts[('ERROR', 'BackendApp')])