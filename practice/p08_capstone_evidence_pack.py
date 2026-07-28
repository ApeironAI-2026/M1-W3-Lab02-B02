# ============================================================
#  PRACTICE p08 -- CAPSTONE: Your Own Evidence Pack   (*)
#  The Cozy Bean  |  M1-W3 Lab02
#
#  THIS IS THE LAST THING YOU WILL BUILD THIS WEEK, AND IT IS THE
#  ONE THAT LOOKS LIKE A REAL JOB.
#
#  YOUR TASK:
#    Mrs Adeyemi has the pack from script 15 -- one row per
#    counterparty. She now asks a different question:
#
#        "Fine. But is this business STEADY?"
#
#    That is a question about TIME, not about counterparties. So
#    build a different feature table: one row per MONTH.
#
#      1. Load and clean the statement. (Reuse your p07 function --
#         that is what it is for.)
#      2. Make a 'month' column from the date.
#      3. Build one row per month with at least four features, e.g.
#         money_in, money_out, txn_count, net, closing balance.
#      4. Save it as engineered_monthly.csv.
#      5. Work out FIVE findings from that table and write them to
#         my_evidence_summary.txt with open().
#
#  THERE IS NO SINGLE CORRECT OUTPUT. The solution has my version
#  so you can compare approach, not answers.
#
#  YOU ARE DONE WHEN:
#    - engineered_monthly.csv exists and has one row per month
#    - my_evidence_summary.txt exists and reads like a person
#      wrote it for another person
#    - every number in it was computed, not typed
#    - it answers "is this business steady?" -- not "who do we pay?"
#
#  HINT: The month column is one line:
#          df['month'] = df['date'].dt.to_period('M').astype(str)
#        Then groupby('month') with named aggregations, exactly as
#        in STEP 14 -- the only thing that changed is what a row
#        MEANS. That is the whole idea.
#        ('last' is a valid aggregation, and it is the one you want
#         for a closing balance.)
#
#  QUESTIONS WORTH ASKING YOUR TABLE:
#    - which month LOOKS biggest -- and why is that misleading?
#      (check what landed on 2026-10-16 before you celebrate)
#    - what is the best month once you set the loan aside?
#    - which was the hardest month, and can you explain it?
#    - did the account ever go overdrawn?
#
#  How to run it: python practice/p08_capstone_evidence_pack.py
#                 (run it from inside the M1-W3-Lab02 folder)
# ============================================================

import numpy as np
import pandas as pd

REVIEW_DATE = pd.Timestamp("2026-11-06")

# TODO 1: load and clean (bring your p07 function with you)
df = pd.read_csv("data/cozybean_statement.csv")

# TODO 2: make the 'month' column

# TODO 3: build the monthly feature table
print("=== MONTHLY FEATURE TABLE ===")
print("(not built yet)")

# TODO 4: save it as engineered_monthly.csv
print("(not saved yet)")

# TODO 5: five findings, written to my_evidence_summary.txt
lines = []
lines.append("=" * 60)
lines.append("   THE COZY BEAN -- MY EVIDENCE SUMMARY")
lines.append(f"   For Mrs Adeyemi  |  Review date {REVIEW_DATE.date()}")
lines.append("=" * 60)
lines.append("")
lines.append("(your five findings go here)")

report = "\n".join(lines)
print(report)
print()
print("(not saved yet)")
