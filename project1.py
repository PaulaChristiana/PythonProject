"""1. How many INFO/DEBUG/ERROR logs per type of app (INFO 2 entries count as one log)"""


from collections import*
import re

def count(file_to_read):
    with open(file_to_read, mode = "r") as file:
        log_data = file.read()
        
        
    log_entries = re.findall(r"\[([A-Z]+)\] - ([\w]+)", log_data) 
    
    log_counts = Counter()
    for log_type, app in log_entries:
        if log_type == "INFO":
            log_counts[(log_type, app)] += 0.5
        else:
            log_counts[(log_type,app)] += 1
    return log_counts
            
    

#log_counts = count("test2.txt")
#print(log_counts)
#print(log_counts[('ERROR', 'BackendApp')])