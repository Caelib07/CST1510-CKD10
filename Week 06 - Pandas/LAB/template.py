"""
RECORD CHECK  -  my version
===========================

Name  : Caelib Kisa-Dhadwal
Lane  : IT      
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import os
import pandas as pd

# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).

scrpit_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(scrpit_dir, "it_data.csv")


df = pd.read_csv(csv_path)  # replace with pd.read_csv("your_file.csv")


# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
#
#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".

# your column(s) go here

df["percent"] = (df["used_gb"] / df["total_gb"]) * 100
df["status"] = df["percent"].apply(lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 else "OK"))



# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.

non_ok_rows = df[df["status"] != "OK"]
print("\n--- Typical Tier Report: Non-OK Records ---")
print(non_ok_rows)


# ==========================================================================
# 4. Before you finish:
#    [ Y ] Run it and check the percent/status columns by hand for one row
#    [ Y ] Check you used & (not "and") if you combined more than one condition
#    [ Y ] Check every column your code refers to actually exists - watch case
