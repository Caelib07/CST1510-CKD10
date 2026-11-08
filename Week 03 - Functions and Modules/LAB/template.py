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

# =================================================================== FUNCTIONS
def status_of(percent):
    """Return the status string based on the utilization percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"
def check(value, limit):
    """Calculate the free space difference and utilization percentage."""
    difference = limit - value
    percent = (value / limit) * 100 if limit > 0 else 0
    return difference, percent

    
# ==================================================================== INPUT
label = input("Enter hostname: ")
value = float(input("Enter GB used: "))
limit = float(input("Enter GB total: "))


# ================================================================== PROCESS

difference, percent = check(value, limit)
status = status_of(percent)


# =================================================================== OUTPUT
  
print()
print("================================")
print(f"  RECORD CHECK  -  {label}")
print("================================")
print(f"  Used       : {value:>9.2f}")
print(f"  Total      : {limit:>9.2f}")
print(f"  Free       : {difference:>9.2f}")
print(f"  Percent    : {percent:>8.2f} %")
print(f"  Status     : {status:>9}")
print("================================")

# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
