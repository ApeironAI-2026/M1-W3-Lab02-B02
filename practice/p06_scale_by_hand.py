# ============================================================
#  PRACTICE p06 -- Scale a Column, By Hand
#  The Cozy Bean  |  M1-W3 Lab02
#
#  YOUR TASK:
#    STEP 13 scaled the debit column. Scale closing_balance
#    instead -- both ways -- using nothing but Week-1 arithmetic.
#      1. Clean closing_balance (commas only; it has no gaps).
#      2. Min-max scale it:  (x - min) / (max - min)
#      3. Z-score scale it:  (x - mean) / std
#      4. Print the min and max of each result.
#      5. Print the mean of the min-max column, and the mean and
#         std of the z-score column.
#      6. Print the HIGHEST balance expressed both ways.
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Original: min 1,615.17  max 52,076.55
#    Min-max:  min 0.0000  max 1.0000
#    Mean of the min-max column: 0.098409
#    Z-score:  mean 0.000000  std 1.000000
#    Z-score:  min -0.8843  max 8.1015
#    Highest balance as min-max: 1.0000
#    Highest balance as z-score: 8.1015
#    Same value, two rulers.
#
#  HINT: No new functions at all. .min(), .max(), .mean(), .std()
#        and the four arithmetic operators you learned in Week 1.
#        Formats: f"{v:,.2f}", f"{v:.4f}", f"{v:.6f}".
#
#  THE INTERESTING BIT: min-max says the biggest balance is 1.0 --
#        "the largest one". Z-score says it is 8.10 -- "eight
#        standard deviations above normal". The second sentence
#        tells you something the first one cannot. That is your
#        answer to "which should I use?": it depends what you want
#        the number to MEAN.
#
#  AND REMEMBER: that z-score formula is the same one you used on a
#        late flight in Lab01. One formula, two completely
#        different jobs.
#
#  How to run it: python practice/p06_scale_by_hand.py
#                 (run it from inside the M1-W3-Lab02 folder)
# ============================================================

import numpy as np
import pandas as pd

df = pd.read_csv("data/cozybean_statement.csv")

# TODO 1: clean closing_balance
print("Original: (not cleaned yet)")

# TODO 2 and 4: min-max scale it, then report min and max
print("Min-max:  (not scaled yet)")

# TODO 5: the mean of the min-max column
print("Mean of the min-max column: (not worked out yet)")

# TODO 3 and 5: z-score scale it, then report mean, std, min, max
print("Z-score:  (not scaled yet)")

# TODO 6: the highest balance, both ways
print("Highest balance as min-max: (not worked out yet)")
print("Highest balance as z-score: (not worked out yet)")
