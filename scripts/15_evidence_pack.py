# ============================================================
#  The Cozy Bean -- Script 15: The Evidence Pack
#  Lab STEP 18 -- the capstone of the week.
#  Shows: all eight features merged into one table, saved as a
#         CSV, plus the one-page note that goes on top of it.
#  Run:   python scripts/15_evidence_pack.py
#         (from M1-W3-Lab02/)
# ============================================================

import numpy as np
import pandas as pd

REVIEW_DATE = pd.Timestamp("2026-11-06")

df = pd.read_csv("data/cozybean_statement.csv")

# ---- clean (STEPs 4-6) --------------------------------------
for col in ['debit', 'credit', 'closing_balance']:
    df[col] = (df[col]
               .astype(str)
               .str.replace(',', '', regex=False)
               .replace({'\\N': np.nan, 'None': np.nan, '': np.nan}))
    df[col] = pd.to_numeric(df[col], errors='coerce')
df['date'] = pd.to_datetime(df['date'], errors='coerce')
rows_all = df.shape[0]
df = df.dropna(subset=['date'])
df = df.fillna({'debit': 0.0, 'credit': 0.0})
df = df[~((df['credit'] == 0) & (df['debit'] == 0))]
df['day_name'] = df['date'].dt.day_name()

# ---- build every feature (STEPs 14-16) ----------------------
money = (df.groupby('counterparty_id', as_index=False)
           .agg(counterparty=('counterparty', 'first'),
                total_debit=('debit', 'sum'),
                total_credit=('credit', 'sum'),
                mean_debit=('debit', 'mean'),
                txn_count=('reference', 'count'),
                active_days=('date', 'nunique'),
                last_txn_date=('date', 'max')))
money['net_position'] = money['total_credit'] - money['total_debit']
money['days_since_last_txn'] = (REVIEW_DATE - money['last_txn_date']).dt.days

rows = []
for cp_id, group in df.groupby('counterparty_id'):
    rows.append({'counterparty_id': cp_id,
                 'busiest_day': group['day_name'].value_counts().idxmax()})
busiest = pd.DataFrame(rows)

# ---- the merge from STEP 17 --------------------------------
features = pd.merge(money, busiest, on='counterparty_id', how='left')
features = features.drop(columns=['last_txn_date'])
for col in ['total_debit', 'total_credit', 'mean_debit', 'net_position']:
    features[col] = features[col].round(2)
features = features.sort_values('net_position', ascending=False)

print("=== THE ENGINEERED FEATURE TABLE ===")
print(features.to_string(index=False))
print()
print(f"Shape: {features.shape[0]} counterparties x {features.shape[1]} features")
print()

features.to_csv("engineered_counterparties.csv", index=False)
print("Saved engineered_counterparties.csv")
print()

# ---- the one-page note (Week-1 f-strings and open()) --------
money_in = df['credit'].sum()
money_out = df['debit'].sum()
tranche = df.nlargest(1, 'credit').iloc[0]
deposit = df.nlargest(1, 'debit').iloc[0]
suppliers = features[features['net_position'] < 0].shape[0]

lines = []
lines.append("=" * 64)
lines.append("   THE COZY BEAN -- EVIDENCE PACK FOR FULL DISBURSEMENT")
lines.append(f"   Prepared for: Mrs Adeyemi   |   Review date: {REVIEW_DATE.date()}")
lines.append("=" * 64)
lines.append("")
lines.append("1. WHAT THIS IS BUILT FROM")
lines.append(f"   Bank statement, {df['date'].min().date()} to {df['date'].max().date()}.")
lines.append(f"   {rows_all} statement lines received; {df.shape[0]} real transactions after")
lines.append("   cleaning (6 unreadable dates dropped, 48 memo lines removed).")
lines.append("")
lines.append("2. THE HEADLINE NUMBERS")
lines.append(f"   Money in over the period:   ${money_in:>12,.2f}")
lines.append(f"   Money out over the period:  ${money_out:>12,.2f}")
lines.append(f"   Net movement:               ${money_in - money_out:>12,.2f}")
lines.append(f"   Lowest balance reached:     ${df['closing_balance'].min():>12,.2f}")
lines.append(f"   Closing balance:            ${df['closing_balance'].iloc[-1]:>12,.2f}")
lines.append("   The account never went overdrawn.")
lines.append("")
lines.append("3. THE TWO LARGEST MOVEMENTS, EXPLAINED")
lines.append(f"   {tranche['date'].date()}  +${tranche['credit']:,.2f}  {tranche['counterparty']}")
lines.append("      -> your first tranche, received and held.")
lines.append(f"   {deposit['date'].date()}  -${deposit['debit']:,.2f}  {deposit['counterparty']}")
lines.append("      -> deposit paid on the branch-two unit.")
lines.append("   Both are flagged as statistical outliers and both are")
lines.append("   expected. Nothing has been removed from this data.")
lines.append("")
lines.append("4. WHO WE TRADE WITH")
lines.append(f"   {features.shape[0]} counterparties over 18 months.")
lines.append(f"   {suppliers} of them are net outflows (suppliers, staff, rent, utilities).")
top = features.nlargest(3, 'total_debit')
lines.append("   Three largest costs:")
for _, r in top.iterrows():
    lines.append(f"      {r['counterparty']:<22} ${r['total_debit']:>11,.2f}  "
                 f"({int(r['txn_count'])} payments)")
lines.append("")
lines.append("5. THE FEATURE TABLE")
lines.append(f"   Attached: engineered_counterparties.csv")
lines.append(f"   {features.shape[0]} rows x {features.shape[1]} columns -- eight engineered features")
lines.append("   per counterparty: totals in and out, net position, average")
lines.append("   payment, transaction count, active days, busiest weekday,")
lines.append("   and days since last activity at the review date.")
lines.append("")
lines.append("PREPARED BY: the owner, The Cozy Bean")
lines.append("STATUS: full disbursement pending your review.")
lines.append("=" * 64)

report = "\n".join(lines)
print(report)

with open("evidence_pack.txt", "w", encoding="utf-8") as f:
    f.write(report + "\n")

print()
print("Saved evidence_pack.txt")
print()
print("Two files. One a machine can read, one a person can read.")
print("That is what a junior data analyst hands a loan officer.")
print("Three weeks ago you had never written a line of Python.")
