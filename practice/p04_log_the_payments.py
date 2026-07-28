# ============================================================
#  PRACTICE p04 -- Log the Payments (Carefully)
#  The Cozy Bean  |  M1-W3 Lab02
#
#  YOUR TASK:
#    STEP 11 logged the debit column. Do the same for CREDIT --
#    the money coming in -- and get the guard right.
#      1. Clean, fill and drop the nothing-happened rows.
#      2. Count how many rows have credit exactly 0.
#      3. Filter to the rows where credit is actually positive.
#      4. Take np.log of those.
#      5. Print min and max before and after, and PROVE there are
#         no infinities in the result.
#      6. Print the spread (max / min) before and after.
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Rows with credit exactly 0: 788
#    Real money-in rows: 604
#    Before -- min 183.54  max 45,000.00
#    After  -- min 5.2124  max 10.7144
#    Any infinities in the logged column? False
#    Spread before: 245x
#    Spread after:  2.1x
#
#  HINT: The guard is one .loc:
#          df.loc[df['credit'] > 0, 'credit']
#        np.isinf(series).any() tells you whether any -inf crept in.
#        Wrap it in bool() so it prints True rather than np.True_.
#        Formats used above: f"{v:,.2f}", f"{v:.4f}", f"{v:,.0f}x",
#        f"{v:.1f}x".
#
#  TRY THE WRONG WAY TOO: comment out the filter and log the whole
#        column. Read the warning numpy gives you. Then look at what
#        min becomes. That is why the filter is not optional.
#
#  How to run it: python practice/p04_log_the_payments.py
#                 (run it from inside the M1-W3-Lab02 folder)
# ============================================================

import numpy as np
import pandas as pd

df = pd.read_csv("data/cozybean_statement.csv")

# TODO 1: clean, fill, drop the nothing-happened rows

# TODO 2: how many rows have credit exactly 0
print("Rows with credit exactly 0: (not counted yet)")

# TODO 3: filter to the positive credits
print("Real money-in rows: (not filtered yet)")

# TODO 4 and 5: log them, and report before/after plus infinities
print("Before -- (not worked out yet)")
print("After  -- (not worked out yet)")
print("Any infinities in the logged column? (not checked yet)")

# TODO 6: the spread, before and after
print("Spread before: (not worked out yet)")
print("Spread after:  (not worked out yet)")
