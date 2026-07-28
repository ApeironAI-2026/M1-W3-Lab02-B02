# ============================================================
#  SOLUTION p04 -- Log the Payments (Carefully)
#  The Cozy Bean  |  M1-W3 Lab02
#
#  How to run it: python solutions/p04_log_the_payments.py
#                 (run it from inside the M1-W3-Lab02 folder)
# ============================================================

import numpy as np
import pandas as pd

df = pd.read_csv("data/cozybean_statement.csv")

for col in ['debit', 'credit']:
    df[col] = (df[col]
               .astype(str)
               .str.replace(',', '', regex=False)
               .replace({'\\N': np.nan, 'None': np.nan, '': np.nan}))
    df[col] = pd.to_numeric(df[col], errors='coerce')
df = df.fillna({'debit': 0.0, 'credit': 0.0})
df = df[~((df['credit'] == 0) & (df['debit'] == 0))]

print("Rows with credit exactly 0:", int((df['credit'] == 0).sum()))

# Filter FIRST. This is the whole point of the exercise.
real_money_in = df.loc[df['credit'] > 0, 'credit']
print("Real money-in rows:", len(real_money_in))

logged = np.log(real_money_in)

print(f"Before -- min {real_money_in.min():,.2f}  max {real_money_in.max():,.2f}")
print(f"After  -- min {logged.min():.4f}  max {logged.max():.4f}")
print("Any infinities in the logged column?", bool(np.isinf(logged).any()))

print(f"Spread before: {real_money_in.max() / real_money_in.min():,.0f}x")
print(f"Spread after:  {logged.max() / logged.min():.1f}x")

# If you had logged the whole column instead of filtering first,
# every zero would have become -inf and numpy would have warned you
# about dividing by zero. -inf is not a small number, it is a
# broken number: it poisons means, breaks histograms, and spreads.
# One .loc filter prevents all of it.
