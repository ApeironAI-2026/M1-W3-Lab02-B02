# ============================================================
#  The Cozy Bean -- Script 03: The First Pass
#  Lab STEP 4.
#  Shows: turning the date column into real dates, finding the
#         six the bank mangled, and the shape of the period.
#  Run:   python scripts/03_eda_pass.py
#         (from M1-W3-Lab02/)
# ============================================================

import pandas as pd

df = pd.read_csv("data/cozybean_statement.csv")

# ---- the date column, converted forgivingly -----------------
print("=== STEP 4: MAKE THE DATES REAL ===")
print("Before:", df['date'].dtype)

df['date'] = pd.to_datetime(df['date'], errors='coerce')

print("After: ", df['date'].dtype)
print()
print("errors='coerce' means: if you cannot read a date, do not")
print("crash -- write NaT instead ('Not a Time') and carry on.")
print()

# ---- did anything fail? -------------------------------------
bad = df['date'].isna().sum()
print(f"Dates the bank's system mangled: {bad}")
print()
print("Here they are, straight from the file:")
raw = pd.read_csv("data/cozybean_statement.csv")
print(raw.loc[df['date'].isna(), ['date', 'reference', 'counterparty']])
print()
print("'not recorded' is not a date. '31/02/2026' is not a date")
print("either -- February does not have 31 days.")
print()

# ---- drop them, and say so ----------------------------------
before = df.shape[0]
df = df.dropna(subset=['date'])
print(f"Rows before: {before}   after dropping the 6: {df.shape[0]}")
print("Six rows out of 1,440 is 0.4%. Dropping them is honest and")
print("cheap. Keeping them would poison every date calculation.")
print()

# ---- the shape of the period --------------------------------
print("=== THE PERIOD WE ARE SHOWING THE BANK ===")
print("First transaction:", df['date'].min().date())
print("Last transaction: ", df['date'].max().date())
print("Days covered:     ", (df['date'].max() - df['date'].min()).days)
print()

print("Busiest five days by number of transactions:")
print(df['date'].value_counts().head())
print()
print("Transactions per day, earliest first (first five days):")
print(df['date'].value_counts().sort_index().head())
