# ============================================================
#  PRACTICE p09 -- BONUS: log1p and Channel Shares
#  The Cozy Bean  |  M1-W3 Lab02
#
#  *** BONUS -- beyond the class session. Nothing depends on
#  *** this file.
#
#  YOUR TASK:
#      1. STEP 11 filtered to debit > 0 before taking np.log.
#         There is another way: np.log1p, which computes
#         log(1 + x) -- so a zero is harmless. Log the WHOLE
#         debit column with it, no filter, and prove there are
#         no infinities.
#      2. Print log1p(0), and the min and max of the result.
#      3. Compare how many values each approach keeps.
#      4. Print what SHARE of transactions used each channel.
#      5. Print what share of the MONEY OUT went through each.
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    np.log1p computes log(1 + x), so a zero is harmless.
#    Rows logged: 1392
#    Any infinities? False
#    log1p(0) = 0.0000
#    min 0.0000  max 10.2577
#    Compare with the filtered plain log from STEP 11:
#      log1p on everything: 1392 values
#      plain log, filtered: 788 values
#    What share of our transactions used each channel?
#    channel
#    transfer          49.8
#    card              40.7
#    standing_order     5.6
#    cash               3.9
#    Name: proportion, dtype: float64
#    And what share of the MONEY OUT went through each?
#           channel  total_debit  share
#    standing_order    198919.79   62.6
#          transfer    117603.92   37.0
#              card      1128.76    0.4
#              cash         0.00    0.0
#
#  HINT: np.log1p(df['debit']) needs no guard at all.
#        value_counts(normalize=True) * 100, then .round(1).
#        For the money share: groupby('channel') with a named
#        aggregation, then divide by the total and round.
#
#  THE THING WORTH NOTICING: those last two tables disagree
#        completely. Standing orders are 5.6% of transactions but
#        62.6% of the money. Counting THINGS and counting MONEY are
#        different questions, and a feature that answers one will
#        mislead you about the other.
#
#  AND THE TRADE-OFF: log1p keeps every row, which is tidy. But
#        log1p(0) is 0.0 -- the same answer it would give a real
#        $0 payment. STEP 11's filter says "those rows are not
#        payments at all" and leaves them out. Both are defensible.
#        Know which question you asked.
#
#  How to run it: python practice/p09_bonus_log1p_and_shares.py
#                 (run it from inside the M1-W3-Lab02 folder)
# ============================================================

import numpy as np
import pandas as pd

df = pd.read_csv("data/cozybean_statement.csv")

# TODO 1: clean, fill, drop the nothing-happened rows

# TODO 2: log1p the whole debit column; report infinities and range
print("np.log1p computes log(1 + x), so a zero is harmless.")
print("Rows logged: (not logged yet)")
print("Any infinities? (not checked yet)")
print("log1p(0) = (not worked out yet)")
print("min (not yet)  max (not yet)")

# TODO 3: compare the two approaches
print("Compare with the filtered plain log from STEP 11:")
print("  (not compared yet)")

# TODO 4: share of transactions per channel
print("What share of our transactions used each channel?")
print("(not worked out yet)")

# TODO 5: share of the money out per channel
print("And what share of the MONEY OUT went through each?")
print("(not worked out yet)")
