# ============================================================
#  SOLUTION p09 -- BONUS: log1p and Channel Shares
#  The Cozy Bean  |  M1-W3 Lab02
#
#  BONUS material -- beyond the class session. Nothing depends
#  on this file.
#
#  How to run it: python solutions/p09_bonus_log1p_and_shares.py
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

# ---- np.log1p: the version that survives a zero -------------
print("np.log1p computes log(1 + x), so a zero is harmless.")

logged = np.log1p(df['debit'])          # no filter needed
print("Rows logged:", len(logged))
print("Any infinities?", bool(np.isinf(logged).any()))
print(f"log1p(0) = {np.log1p(0):.4f}")
print(f"min {logged.min():.4f}  max {logged.max():.4f}")

filtered = np.log(df.loc[df['debit'] > 0, 'debit'])
print("Compare with the filtered plain log from STEP 11:")
print(f"  log1p on everything: {len(logged)} values")
print(f"  plain log, filtered: {len(filtered)} values")

# ---- channel shares -----------------------------------------
print("What share of our transactions used each channel?")
print((df['channel'].value_counts(normalize=True) * 100).round(1))

print("And what share of the MONEY OUT went through each?")
by_channel = df.groupby('channel', as_index=False).agg(
    total_debit=('debit', 'sum'))
by_channel['share'] = (by_channel['total_debit']
                       / by_channel['total_debit'].sum() * 100).round(1)
print(by_channel.sort_values('share', ascending=False).to_string(index=False))

# log1p keeps every row, which is tidy -- but it quietly changes what
# the numbers MEAN. log1p(0) is 0.0, the same answer you would get for
# a $0 payment and for no payment at all. STEP 11's filter says "these
# rows are not payments" and leaves them out. Both are defensible;
# just know which question you asked.
#
# And notice the two share tables disagree completely: standing orders
# are only a few per cent of transactions but a huge share of the
# money. Counting things and counting money are different questions.
