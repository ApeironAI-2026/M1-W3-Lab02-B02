# ============================================================
#  The Cozy Bean -- Script 12: The First Five Features
#  Lab STEPs 14-15.
#  Shows: named aggregation -- one row per counterparty, and a
#         column for each thing you want to know about them.
#  Run:   python scripts/12_features_totals.py
#         (from M1-W3-Lab02/)
# ============================================================

import numpy as np
import pandas as pd

df = pd.read_csv("data/cozybean_statement.csv")

# Pick up where STEPs 5-6 left off.
for col in ['debit', 'credit', 'closing_balance']:
    df[col] = (df[col]
               .astype(str)
               .str.replace(',', '', regex=False)
               .replace({'\\N': np.nan, 'None': np.nan, '': np.nan}))
    df[col] = pd.to_numeric(df[col], errors='coerce')
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df = df.dropna(subset=['date'])
df = df.fillna({'debit': 0.0, 'credit': 0.0})
df = df[~((df['credit'] == 0) & (df['debit'] == 0))]

# ---- Feature 1 & 2  (STEP 14): money in, money out ----------
print("=== STEP 14: FEATURES 1 AND 2 -- THE TOTALS ===")
print("One row per counterparty. Who pays us, who we pay.")
print()

totals = (
    df.groupby('counterparty_id', as_index=False)
      .agg(
          total_debit=('debit', 'sum'),
          total_credit=('credit', 'sum'),
      )
)

print(totals.round(2).to_string(index=False))
print()
print("Read the syntax once and you own it for life:")
print("    total_debit=('debit', 'sum')")
print("     ^new column   ^old column  ^what to do to it")
print()
print("This is a NAMED aggregation. You name the column you want")
print("and say how to build it. No two-level headers, no flattening.")
print()

# ---- Feature 3  (STEP 15): net position ---------------------
print("=== STEP 15: FEATURE 3 -- NET POSITION ===")
totals['net_position'] = totals['total_credit'] - totals['total_debit']
print("A column built from two other columns. No groupby needed --")
print("just arithmetic, exactly like Week 1.")
print()

# ---- Feature 4 & 5: the average, and how often --------------
print("=== STEP 15: FEATURES 4 AND 5 -- AVERAGE AND COUNT ===")
more = (
    df.groupby('counterparty_id', as_index=False)
      .agg(
          mean_debit=('debit', 'mean'),
          txn_count=('reference', 'count'),
      )
)
totals = totals.merge(more, on='counterparty_id', how='left')

names = df.groupby('counterparty_id', as_index=False).agg(
    counterparty=('counterparty', 'first'))
table = names.merge(totals, on='counterparty_id', how='left')

print(table.round(2).to_string(index=False))
print()

print("=== WHAT THESE FIVE COLUMNS ALREADY TELL MRS ADEYEMI ===")
biggest_in = table.nlargest(1, 'total_credit').iloc[0]
biggest_out = table.nlargest(1, 'total_debit').iloc[0]
busiest = table.nlargest(1, 'txn_count').iloc[0]
print(f"  Our biggest source of money: {biggest_in['counterparty']} "
      f"(${biggest_in['total_credit']:,.2f})")
print(f"  Our biggest cost:            {biggest_out['counterparty']} "
      f"(${biggest_out['total_debit']:,.2f})")
print(f"  Who we deal with most often: {busiest['counterparty']} "
      f"({int(busiest['txn_count'])} transactions)")
print()
print("Five columns. Twelve rows. That is a business, described.")
print()
print("HONESTLY, THOUGH: the class notebook built 45 of these in one")
print("giant 100-line loop. That is a working data scientist's version")
print("of exactly what you just did by hand -- same idea, more of it.")
print("You are not doing a simplified version. You are doing the")
print("readable version.")
