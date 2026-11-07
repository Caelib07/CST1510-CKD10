"""
RECORD CHECK  -  my version
===========================

Name  :  Caelib Kisa-Dhadwal
Lane  :  IT   
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here

def check_record(value, limit):
    """Calculate the difference, completion percentage, and limit status of a record."""
    difference = value - limit 
    percent = (value / limit) * 100 if limit > 0 else 0

    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"

    return difference, percent, status 

def print_report(label, value, limit, difference, percent, status):
    """Format and print the record analysis directly to the terminal."""
    print(f"Hostname: {label}")
    print(f"Storage Used: {value} GB / Total: {limit} GB")
    print(f"Difference: {difference} GB ({percent:.1f}%)")
    print(f"Status: {status}")
    print("-" * 30)

def load_records(path):
    """Load IT records from a file, returning a list of structured dictionaries."""
    loaded_list = []
    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            if len(parts) == 3:
                record = {
                    "label": parts[0],
                    "value": int(parts[1]),
                    "limit": int(parts[2])    
                }
                loaded_list.append(record)
    return loaded_list

def save_results(path, results):
    """Write the final label and status reports out to a new text file."""
    with open(path, 'w') as file:
        for label, status in results:
            file.write(f"{label},{status}\n")


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
try:
    records = load_records("it_data.txt")
except FileNotFoundError:
    print("Error: The data file 'it_data.txt' was not found.")
    print("Starting program with an empty records list.")
    records = []
 


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here

over_limit_count = 0
output_results = []

for rec in records:
    diff, pct, stat = check_record(rec["value"], rec["limit"])
    
    print_report(rec["label"], rec["value"], rec["limit"], diff, pct, stat)
    
    if stat == "OVER LIMIT":
        over_limit_count += 1
 
    output_results.append((rec["label"], stat))
 
if records:
    save_results("it_results.txt", output_results)
    print(f"Total systems OVER LIMIT: {over_limit_count}")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
