# ============================================================
#  The Cozy Bean -- Script 14: Stapling Two Tables Together
#  Lab STEP 17.
#  Shows: pd.merge -- the one move that turns several small
#         summary tables into one feature table.
#  Run:   python scripts/14_meet_merge.py
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

# ---- two small tables, built separately ---------------------
totals = (
    df.groupby('counterparty_id', as_index=False)
      .agg(total_debit=('debit', 'sum'),
           total_credit=('credit', 'sum'))
)

counts = (
    df.groupby('counterparty_id', as_index=False)
      .agg(txn_count=('reference', 'count'),
           active_days=('date', 'nunique'))
)

print("=== STEP 17: TWO TABLES, ONE SHARED COLUMN ===")
print()
print("TABLE A -- the money (first four rows):")
print(totals.head(4).round(2).to_string(index=False))
print()
print("TABLE B -- the activity (first four rows):")
print(counts.head(4).to_string(index=False))
print()
print("Both have a 'counterparty_id' column. That shared column is")
print("the KEY, and it is what lets us staple them together.")
print()

# ---- the merge ----------------------------------------------
print("=== ONE LINE ===")
print("    merged = pd.merge(totals, counts, on='counterparty_id', how='left')")
print()

merged = pd.merge(totals, counts, on='counterparty_id', how='left')

print(merged.round(2).to_string(index=False))
print()
print(f"Table A had {totals.shape[1]} columns. Table B had {counts.shape[1]}.")
print(f"The merged table has {merged.shape[1]} -- the key is not repeated.")
print(f"Rows: {totals.shape[0]} in, {merged.shape[0]} out. Nothing lost.")
print()

# ---- what how='left' actually promises ----------------------
print("=== WHAT how='left' MEANS ===")
print("'Keep every row from the LEFT table, and bring over matches")
print("from the right.' The left table is the one you named first.")
print()
print("It matters when the right table is missing somebody. Watch:")
print()

partial = counts[counts['counterparty_id'] != 'c8']
print("Table B with c8 (the loan) deliberately removed, then merged:")
demo = pd.merge(totals, partial, on='counterparty_id', how='left')
print(demo[demo['counterparty_id'] == 'c8'].to_string(index=False))
print()
print("c8 survived -- because it was in the left table -- but its")
print("right-hand columns are NaN. how='left' keeps the row and admits")
print("it does not know. That is usually exactly what you want, and")
print("it is why a merge can quietly introduce new gaps.")
print()
print("Always check isna().sum() after a merge. Always.")
print("Gaps introduced by that merge:", int(demo.isna().sum().sum()))
