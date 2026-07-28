# ============================================================
#  SOLUTION p06 -- Scale a Column, By Hand
#  The Cozy Bean  |  M1-W3 Lab02
#
#  How to run it: python solutions/p06_scale_by_hand.py
#                 (run it from inside the M1-W3-Lab02 folder)
# ============================================================

import numpy as np
import pandas as pd

df = pd.read_csv("data/cozybean_statement.csv")

df['closing_balance'] = (df['closing_balance']
                         .astype(str)
                         .str.replace(',', '', regex=False))
df['closing_balance'] = pd.to_numeric(df['closing_balance'], errors='coerce')

balance = df['closing_balance']

# ---- min-max ------------------------------------------------
minmax = (balance - balance.min()) / (balance.max() - balance.min())

print(f"Original: min {balance.min():,.2f}  max {balance.max():,.2f}")
print(f"Min-max:  min {minmax.min():.4f}  max {minmax.max():.4f}")
print(f"Mean of the min-max column: {minmax.mean():.6f}")

# ---- z-score ------------------------------------------------
z = (balance - balance.mean()) / balance.std()

print(f"Z-score:  mean {z.mean():.6f}  std {z.std():.6f}")
print(f"Z-score:  min {z.min():.4f}  max {z.max():.4f}")

# ---- the highest balance, both ways -------------------------
print(f"Highest balance as min-max: {minmax.max():.4f}")
print(f"Highest balance as z-score: {z.max():.4f}")

print("Same value, two rulers.")

# min-max always gives you exactly 0 and exactly 1 at the ends --
# useful when you need a guaranteed range. z-score always gives you
# mean 0 and std 1 -- useful when you care how UNUSUAL a value is.
# A z-score of 8 says "eight standard deviations out"; a min-max of
# 1.0 only says "this was the biggest one". Different questions.
