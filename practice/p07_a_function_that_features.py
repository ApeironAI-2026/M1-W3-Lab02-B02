# ============================================================
#  PRACTICE p07 -- The Function That Ends the Copy-Pasting   (*)
#  The Cozy Bean  |  M1-W3 Lab02
#
#  YOU HAVE EARNED THIS ONE.
#
#  Every script from 06 onwards in scripts/ starts with the same
#  nine lines of cleaning. You have now read them about eight
#  times. That irritation is the lesson: repetition is the signal
#  that a function is missing.
#
#  YOUR TASK:
#      1. Write load_clean_statement(path) that reads the CSV and
#         does EVERY cleaning move from STEPs 4-6, then RETURNS
#         the clean DataFrame.
#      2. Write build_features(df) that returns one row per
#         counterparty with: counterparty, total_debit,
#         total_credit, txn_count, and net_position.
#      3. Call them both. Print the clean row count, the feature
#         table's shape, the table itself, and who has the best
#         net position.
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Clean rows: 1387
#    Feature table shape: (12, 6)
#    counterparty_id         counterparty  total_debit  total_credit  txn_count  net_position
#                 c1      Card Settlement         0.00     271116.53        546     271116.53
#                c10         Cash Deposit         0.00      17086.67         53      17086.67
#                c11    Card Machine Fees      1128.76          0.00         18      -1128.76
#                c12 Insurance & Licences      2346.06          0.00          6      -2346.06
#                 c2     Beans Direct Ltd     31682.99          0.00        167     -31682.99
#                 c3             Dairy Co     31272.79          0.00        298     -31272.79
#                 c4    Muffin Top Bakery     25901.43          0.00        225     -25901.43
#                 c5    Cozy Bean Payroll    158770.11          0.00         36    -158770.11
#                 c6   Riverside Lettings     33300.00          0.00         18     -33300.00
#                 c7           City Power      4503.62          0.00         18      -4503.62
#                 c8    Aperion Bank Loan         0.00      45000.00          1      45000.00
#                 c9   Northgate Property     28500.00          0.00          1     -28500.00
#    Best net position: Card Settlement (271,116.53)
#
#  HINT: The cleaning function needs, in this order: the money loop,
#        to_datetime with errors='coerce', dropna on date, fillna
#        with 0 for debit and credit, and the ~ filter.
#        The feature function is ONE named aggregation plus one
#        arithmetic line for net_position.
#        Print with .round(2).to_string(index=False).
#
#  WHY 1387 AND NOT 1392? Because dropping the six mangled dates
#        removes five more rows on top of the 48 memo lines -- one
#        of the six was already a memo line. Small numbers like
#        that are worth chasing down rather than shrugging at.
#
#  How to run it: python practice/p07_a_function_that_features.py
#                 (run it from inside the M1-W3-Lab02 folder)
# ============================================================

import numpy as np
import pandas as pd


# TODO 1: write load_clean_statement(path) -> clean DataFrame
def load_clean_statement(path):
    return pd.read_csv(path)


# TODO 2: write build_features(df) -> one row per counterparty
def build_features(df):
    return pd.DataFrame()


statement = load_clean_statement("data/cozybean_statement.csv")
print("Clean rows:", statement.shape[0])

table = build_features(statement)
print("Feature table shape:", table.shape)
print("(no features built yet)")

# TODO 3: print the table and the best net position
print("Best net position: (not worked out yet)")
