"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here

def parse_line(raw_line):
    """Clean and parse a messy IT log line into a structured dictionary."""
    # Strips whitespace and lowercase the entire line
    clean_line = raw_line.strip().lower()
    
    # Splits the hostname away from the remaining metric units
    hostname_part, rest = clean_line.split(",", 1)
    record_dict = {"hostname": hostname_part.strip()}
    
    # Splits the remaining metric pairs with commas 
    for piece in rest.split(","):
        if "=" in piece:
            key, value = piece.split("=")
            record_dict[key.strip()] = float(value.strip())
            
    return record_dict
def status_of(parsed_record):
    """Calculate storage consumption percentage and return threshold classification status."""
    percent = (parsed_record["used"] / parsed_record["total"]) * 100
    
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

raw_records = [
    "  Srv-01 , used=87 , total=100  ",
    "SRV-02,USED=120,TOTAL=120",
    "   srv-03   ,   used=45,total=100",
    "srv-04, used=95 ,total=100   ",
    "  SRV-05 ,used=105 , total=100"
]


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

print("--- Typical Tier Report: String Parsing & Status Verification ---")
print(f"{'Cleaned Dictionary':<55} | {'Status Evaluation'}")
print("-" * 80)

# Process and report on every record using our functions
for raw_record in raw_records:
    
    cleaned_data = parse_line(raw_record)
    current_status = status_of(cleaned_data)
    print(f"{str(cleaned_data):<55} | {current_status}")



# ==========================================================================
# 4. Before you finish:
#
#    [ Y ] Run it against at least 5 genuinely messy raw records
#    [ Y ] Run it with a value that will not convert to a number - write the
#        error down
#    [ Y ] Check every function does one job, with a docstring
