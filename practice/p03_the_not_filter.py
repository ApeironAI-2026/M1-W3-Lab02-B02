# ============================================================
#  PRACTICE p03 -- The NOT Filter
#  The Cozy Bean  |  M1-W3 Lab02
#
#  YOUR TASK:
#    Prove to yourself that ~ does what you think it does, by
#    writing the same filter two different ways.
#      1. Clean debit and credit and fill their gaps with 0.
#      2. Count the rows where BOTH are zero.
#      3. Drop them using ~ (NOT).
#      4. Drop them again WITHOUT using ~ -- using != and | .
#      5. Prove the two answers match.
#      6. Count the counterparties before and after.
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Rows to start with: 1440
#    Rows where nothing moved: 48
#    Kept with ~ : 1392
#    Kept the long way: 1392
#    Same answer? True
#    Counterparties before: 13
#    Counterparties after:  12
#
#  HINT: The ~ version:
#          df[~((df['credit'] == 0) & (df['debit'] == 0))]
#        The long version says the same thing inside out:
#          df[(df['credit'] != 0) | (df['debit'] != 0)]
#        "NOT (both zero)" is the same as "either one is not zero".
#
#  WORTH KNOWING: that equivalence has a name -- De Morgan's law.
#        You do not need the name. You do need to notice that ~ is
#        shorter AND reads closer to what you actually meant.
#
#  How to run it: python practice/p03_the_not_filter.py
#                 (run it from inside the M1-W3-Lab02 folder)
# ============================================================

import numpy as np
import pandas as pd

df = pd.read_csv("data/cozybean_statement.csv")

# TODO 1: clean debit and credit, fill gaps with 0.0
print("Rows to start with:", df.shape[0])

# TODO 2: count the rows where nothing moved
print("Rows where nothing moved: (not counted yet)")

# TODO 3: drop them with ~
print("Kept with ~ : (not filtered yet)")

# TODO 4: drop them without ~
print("Kept the long way: (not filtered yet)")

# TODO 5: prove they match
print("Same answer? (not checked yet)")

# TODO 6: counterparties before and after
print("Counterparties before: (not counted yet)")
print("Counterparties after:  (not counted yet)")
