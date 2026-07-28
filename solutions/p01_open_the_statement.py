# ============================================================
#  SOLUTION p01 -- Open the Statement
#  The Cozy Bean  |  M1-W3 Lab02
#
#  How to run it: python solutions/p01_open_the_statement.py
#                 (run it from inside the M1-W3-Lab02 folder)
# ============================================================

import pandas as pd

df = pd.read_csv("data/cozybean_statement.csv")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("Column names:", list(df.columns))

print("How many columns did pandas load as text?",
      len(df.select_dtypes(include='str').columns))
print("How many as numbers?",
      len(df.select_dtypes(include='number').columns))

print("Counterparties in the file:", df['counterparty_id'].nunique())
print("Channels in the file:", sorted(df['channel'].unique()))

# Every single column is text -- including all three money columns
# and the date. Nothing numeric survived the bank's export, which
# is exactly the problem STEPs 4-6 exist to solve.
