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

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

# your class goes here

class Record:
    def __init__(self, hostname, gb_used, gb_total):
        #setting attributes 
        self.hostname = hostname
        self.gb_used = gb_used
        self.gb_total = gb_total

    def status(self):
        """Return the usage status based on the percentage of GB used."""
        percentage = (self.gb_used / self.gb_total) * 100

        if percentage >= 100:
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.

# your records go here
r1 = Record("srv-01", 87, 120)
r2 = Record("srv-02", 115, 120)
r3 = Record("srv-03", 130, 120)

all_records = [r1, r2, r3]


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)
for record in all_records:
    current_status = record.status()
    
    print()
    print("=" * 34)
    print(f" RECORD CHECK - {record.hostname}")
    print("=" * 34)
    
    print(f"| Storage Used:  {record.gb_used:>4} GB         |")
    print(f"| Storage Limit: {record.gb_total:>4} GB         |")
    print(f"| Status:        {current_status:<14} |")
    
    print("=" * 34)
   
 


# ==========================================================================
# 4. Before you finish:
#
#    [ Y ] Run it and check every record's numbers by hand
#    [ Y ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ Y ] Check every method and __init__ has a one-line docstring
