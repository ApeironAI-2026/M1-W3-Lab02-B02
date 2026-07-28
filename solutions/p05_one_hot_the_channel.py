# ============================================================
#  SOLUTION p05 -- One-Hot the Channel Column
#  The Cozy Bean  |  M1-W3 Lab02
#
#  How to run it: python solutions/p05_one_hot_the_channel.py
#                 (run it from inside the M1-W3-Lab02 folder)
# ============================================================

import pandas as pd

df = pd.read_csv("data/cozybean_statement.csv")

print("Channel values:", sorted(df['channel'].unique()))
print("How many of each:")
print(df['channel'].value_counts())

encoded = pd.get_dummies(df['channel'], prefix='channel').astype(int)

print("New columns:", list(encoded.columns))
print("Shape of the encoded block:", encoded.shape)

print("First three rows:")
print(encoded.head(3))

# Every row must have exactly one 1 -- that is the ONE in one-hot.
row_totals = encoded.sum(axis=1)
print("Rows whose 0/1 columns add up to exactly 1:",
      int((row_totals == 1).sum()), "of", len(encoded))

print("Column totals match the original counts:")
print(encoded.sum())

# The column totals are the same numbers as value_counts() above,
# just in alphabetical order instead of biggest-first. That is a
# good sanity check after any encoding: no rows invented, none lost.
