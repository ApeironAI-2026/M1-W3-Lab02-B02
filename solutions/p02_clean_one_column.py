# ============================================================
#  SOLUTION p02 -- Clean One Column, Four Moves
#  The Cozy Bean  |  M1-W3 Lab02
#
#  How to run it: python solutions/p02_clean_one_column.py
#                 (run it from inside the M1-W3-Lab02 folder)
# ============================================================

import numpy as np
import pandas as pd

df = pd.read_csv("data/cozybean_statement.csv")

print("Before -- dtype:", df['closing_balance'].dtype)
print("A cell with a comma in it:", repr(df['closing_balance'].iloc[0]))

# The four moves, in order.
df['closing_balance'] = df['closing_balance'].astype(str)
df['closing_balance'] = df['closing_balance'].str.replace(',', '', regex=False)
df['closing_balance'] = df['closing_balance'].replace(
    {'\\N': np.nan, 'None': np.nan, '': np.nan})
df['closing_balance'] = pd.to_numeric(df['closing_balance'], errors='coerce')

print("After -- dtype:", df['closing_balance'].dtype)
print("Gaps:", int(df['closing_balance'].isna().sum()))
print(f"Lowest balance:  {df['closing_balance'].min():,.2f}")
print(f"Highest balance: {df['closing_balance'].max():,.2f}")
print(f"Mean balance:    {df['closing_balance'].mean():,.2f}")

# closing_balance is the easy one: the bank printed a running
# balance on every single line, so there are no gaps at all. Its
# only problem was the commas. Beats 3 and 4 still ran -- they
# just had nothing to do, which is what defensive code looks like.
