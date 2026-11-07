"""
RECORD CHECK  -  my version
===========================

Name  : Caelib Kisa-Dhadwal 
Lane  :  IT      
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
import math
# =================================================================== FUNCTIONS
def status_of(percent):
    """Return the status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARINING"
    else:
        return "OK"

def check(value, limit):
    """Calculate the difference and percentage."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent

def print_report(label, value, limit, difference, percent, status):
    """Print the complete formatted report with borders."""
    print()
    print("-" * 34)
    print(f" RECORD CHECK  -  {label}")
    print("-" * 34)
    print(f"Used         :   {value:>9.2f}")
    print(f"Total        :   {limit:>9.2f}")
    print(f"Free         :   {difference:>9.2f}")
    print(f"Percent      :   {percent:>8.2f} %")
    print(f"Status       :   {status:>9}")
    print("-" * 34)

over_limit_count = 0

while True:
# ==================================================================== INPUT
    label = input("\nEnter hostname (or 'quit' to stop): ")

    if label.lower() == "quit":
        break

    value = float(input("Enter GB used: "))
    limit = float(input("Enter GB total: "))


# ================================================================== PROCESS
    difference, percent = check(value, limit)
    status = status_of(percent)

    if status == "OVER LIMIT":
        over_limit_count += 1


# =================================================================== OUTPUT
  
print_report(label, value, limit, difference, percent, status)

print()
print(f"Records OVER LIMIT: {over_limit_count}")

# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
