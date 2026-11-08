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

# Giving each a one-line docstring.

def check_record(value,limit):
    """Calculate the difference, the completion percentage, and the limit status of a record."""
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
    print(f"Difference: {difference} GB ({percent:.1f}%")
    print(f"Status: {status}")

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

import os

# This automatically finds the exact folder where template.py is sitting
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "records_sample.txt")

records = load_records(file_path)



# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here

for rec in records:
    # 1. Run the calculations
    diff, pct, stat = check_record(rec["value"], rec["limit"])
    
    # 2. Print out the formatted report block
    print_report(rec["label"], rec["value"], rec["limit"], diff, pct, stat)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
