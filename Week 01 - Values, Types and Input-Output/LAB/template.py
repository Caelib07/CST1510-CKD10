"""
RECORD CHECK  -  my version
===========================

Name  : Caelib Kisa - Dhadwal
Lane  :  IT      
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.

hostname = input("Enter hostname: ")
gb_used = float(input("Enter GB used: "))
gb_total = float(input("Enter GB total: "))


# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]


#Remaining storage space calculation
gb_free = gb_total - gb_used

#Total space used as a percentage
percentage_used = (gb_used / gb_total) * 100

#Calcualtes the over-provisioning multiplier to tell you how many times it is larger then the toatal
capacity_multiplier = gb_total / gb_used


# =================================================================== OUTPUT
# 3. Print the report.

print()
print("-" * 34)
print(f"  RECORD CHECK  -  {hostname}")
print("-" * 34)

print(f"Used         : {gb_used:>10.2f}")
print(f"Total        : {gb_total:>10.2f}")
# The '+' flag satisfies the signed difference requirement
print(f"Free       : {gb_free:>+10.2f}")
print(f"Percent    : {percentage_used:>10.2f} %")



print(f"Multiplier : {capacity_multiplier:>10.2f}x")
print("-" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
