# ============================================================
#  SOLUTION p03 -- The NOT Filter
#  The Cozy Bean  |  M1-W3 Lab02
#
#  How to run it: python solutions/p03_the_not_filter.py
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

print("Rows to start with:", df.shape[0])

nothing_happened = (df['credit'] == 0) & (df['debit'] == 0)
print("Rows where nothing moved:", int(nothing_happened.sum()))

# Two ways to say the same thing.
kept_with_not = df[~nothing_happened]
kept_the_long_way = df[(df['credit'] != 0) | (df['debit'] != 0)]

print("Kept with ~ :", kept_with_not.shape[0])
print("Kept the long way:", kept_the_long_way.shape[0])
print("Same answer?", kept_with_not.shape[0] == kept_the_long_way.shape[0])

print("Counterparties before:", df['counterparty_id'].nunique())
print("Counterparties after: ", kept_with_not['counterparty_id'].nunique())

# NOT (A AND B) is the same as (NOT A) OR (NOT B) -- which is why
# the ~ version and the long version agree exactly. The ~ version
# is shorter and reads closer to what you meant: "drop the rows
# where nothing happened."
#
# And c0 disappears entirely, because the memo lines were the only
# rows with zero on both sides. 13 counterparties become 12.
