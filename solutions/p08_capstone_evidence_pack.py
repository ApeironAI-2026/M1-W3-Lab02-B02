# ============================================================
#  SOLUTION p08 -- CAPSTONE: Your Own Evidence Pack
#  The Cozy Bean  |  M1-W3 Lab02
#
#  There is no single right answer. This is MY version. Yours
#  will pick different features and say different things, and
#  that is exactly right -- what matters is that it is honest,
#  computed, and readable by a person.
#
#  One trick to steal: the loan month (2026-10) is split OUT
#  before any conclusion gets drawn. One extraordinary month
#  will otherwise silently own every average and every "best".
#  Same lesson as STEP 10's outlier -- explain it, never let it
#  masquerade as trading.
#
#  How to run it: python solutions/p08_capstone_evidence_pack.py
#                 (run it from inside the M1-W3-Lab02 folder)
# ============================================================

import numpy as np
import pandas as pd

REVIEW_DATE = pd.Timestamp("2026-11-06")
LOAN_MONTH = "2026-10"          # the tranche AND the deposit both land here


def load_clean_statement(path):
    df = pd.read_csv(path)
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
    return df


df = load_clean_statement("data/cozybean_statement.csv")
df['month'] = df['date'].dt.to_period('M').astype(str)

# ---- MY choice: features per MONTH, not per counterparty -----
monthly = (
    df.groupby('month', as_index=False)
      .agg(money_in=('credit', 'sum'),
           money_out=('debit', 'sum'),
           txn_count=('reference', 'count'),
           closing=('closing_balance', 'last'))
)
monthly['net'] = (monthly['money_in'] - monthly['money_out']).round(2)
monthly['money_in'] = monthly['money_in'].round(2)
monthly['money_out'] = monthly['money_out'].round(2)

print("=== MONTHLY FEATURE TABLE ===")
print(monthly.to_string(index=False))
print()

monthly.to_csv("engineered_monthly.csv", index=False)
print("Saved engineered_monthly.csv")
print()

# ---- split the loan month out BEFORE drawing conclusions -----
trading = monthly[monthly['month'] != LOAN_MONTH]
loan_row = monthly[monthly['month'] == LOAN_MONTH].iloc[0]

tranche = df.loc[df['counterparty_id'] == 'c8', 'credit'].sum()
deposit = df.loc[df['counterparty_id'] == 'c9', 'debit'].sum()
oct_trading_net = loan_row['net'] - tranche + deposit

best = trading.nlargest(1, 'money_in').iloc[0]
worst = trading.nsmallest(1, 'net').iloc[0]

# The narrative clauses below ("the Christmas rush", the February
# insurance bill) were checked against the shipped statement, not
# assumed: best trading month IS 2025-12, and the quarterly
# insurance payment DOES land on the 8th of February.
lines = []
lines.append("=" * 60)
lines.append("   THE COZY BEAN -- MY EVIDENCE SUMMARY")
lines.append(f"   For Mrs Adeyemi  |  Review date {REVIEW_DATE.date()}")
lines.append("=" * 60)
lines.append("")
lines.append(f"FINDING 1: {monthly.shape[0]} months, {df.shape[0]} real transactions.")
lines.append(f"           Setting the loan month aside, a trading month")
lines.append(f"           brings in ${trading['money_in'].mean():,.2f} on average.")
lines.append("")
lines.append(f"FINDING 2: The table's biggest month is {loan_row['month']}")
lines.append(f"           (${loan_row['money_in']:,.2f}) -- but ${tranche:,.2f} of that")
lines.append(f"           is your tranche, not trading. The best TRADING")
lines.append(f"           month was {best['month']} (${best['money_in']:,.2f}):")
lines.append("           the Christmas rush.")
lines.append("")
lines.append(f"FINDING 3: Costs are steady. Money out stays between")
lines.append(f"           ${trading['money_out'].min():,.2f} and ${trading['money_out'].max():,.2f} every single")
lines.append("           trading month. The swings are all on the income")
lines.append("           side, and they follow the seasons.")
lines.append("")
lines.append(f"FINDING 4: The hardest month was {worst['month']} (net ${worst['net']:,.2f}):")
lines.append("           the short, quiet month after Christmas, with the")
lines.append("           quarterly insurance bill landing in it. The")
lines.append("           account absorbed it without drama.")
lines.append("")
lines.append(f"FINDING 5: The account never went overdrawn in 18 months.")
lines.append(f"           Lowest point: ${df['closing_balance'].min():,.2f}. And with the")
lines.append(f"           tranche and deposit set aside, {LOAN_MONTH}'s own")
lines.append(f"           trading still came out at +${oct_trading_net:,.2f} --")
lines.append("           the shop that earned the tranche is still trading")
lines.append("           like it.")
lines.append("")
lines.append("CONCLUSION: the trading pattern that earned the first")
lines.append("tranche has not changed. Attached: engineered_monthly.csv")
lines.append("=" * 60)

report = "\n".join(lines)
print(report)

with open("my_evidence_summary.txt", "w", encoding="utf-8") as f:
    f.write(report + "\n")

print()
print("Saved my_evidence_summary.txt")

# Grouping by MONTH instead of counterparty answers a completely
# different question -- "is this business steady?" rather than
# "who do we trade with?". Choosing what a row MEANS is the first
# and most important decision in feature engineering.
