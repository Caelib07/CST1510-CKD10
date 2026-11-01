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

# ==================================================================== INPUT
over_limit_count = 0
while True:

    label = input("\nEnter hostname (or 'quit' to stop):")

    if label.lower() == "quit":
        break
    value = float(input("Enter GB used: "))
    limit = float(input("Enter GB total: "))



# ================================================================== PROCESS
difference = limit - value
percent = (value / limit) * 100

if percent >= 100:
    status = "OVER LIMIT"
    over_limit_count += 1
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"


# =================================================================== OUTPUT
# 4. Print the report.
#
 

print()
print("-" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# your report lines go here
print(f"Used         :   {value:>9.2f}")
print(f"Total        :   {limit:>9.2f}")
print(f"Free         :   {difference:>9.2f}")
print(f"Percent      :   {percent:>8.2f} %")
print(f"Status       :   {status:>9}")

print("-" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
