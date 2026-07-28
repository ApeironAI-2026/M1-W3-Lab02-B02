# ============================================================
#  The Cozy Bean -- Script 08: Outlier, or Loan?
#  Lab STEP 10.
#  Shows: Lab01's IQR method pointed at your own money -- and a
#         judgement call that a formula cannot make for you.
#  Run:   python scripts/08_outlier_or_loan.py
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

# ---- the same four lines as Lab01 STEP 13 -------------------
print("=== STEP 10: THE IQR FENCE, ON YOUR OWN MONEY ===")
Q1 = df['credit'].quantile(0.25)
Q3 = df['credit'].quantile(0.75)
IQR = Q3 - Q1

print(f"Q1  = {Q1}")
print(f"Q3  = {round(Q3, 2)}")
print(f"IQR = {round(IQR, 2)}")
print(f"Upper fence (Q3 + 1.5 * IQR) = ${round(Q3 + 1.5 * IQR, 2)}")
print()

outliers = df[
    (df['credit'] < Q1 - 1.5 * IQR) |
    (df['credit'] > Q3 + 1.5 * IQR)
]

print("Credits the formula flags as outliers:", outliers.shape[0])
print()
print(outliers[['date', 'credit', 'counterparty', 'reference']].to_string(index=False))
print()

# ---- the judgement call -------------------------------------
print("=== NOW THE PART NO FORMULA CAN DO ===")
print("The maths flagged exactly one row in eighteen months. And it")
print("is not an error, a typo, or a fraud. It is the single most")
print("important line in the entire file: Mrs Adeyemi's first tranche.")
print()
print("A technique like this was described in class as one that")
print("then removes them'. Do NOT remove this one. If you delete it,")
print("you delete the evidence that the bank already believes in you.")
print()
print("So: FLAG it, explain it, keep it. Add a column saying so.")
print()

df['flagged'] = False
df.loc[outliers.index, 'flagged'] = True
df['flag_reason'] = ""
df.loc[outliers.index, 'flag_reason'] = "large credit - loan tranche, expected"

print(df.loc[outliers.index,
             ['date', 'credit', 'counterparty', 'flagged', 'flag_reason']]
      .to_string(index=False))
print()
print("Flagged rows kept in the table:", int(df['flagged'].sum()))
print("Rows deleted:", 0)
print()
print("An outlier is a QUESTION, not a verdict. This one had a")
print("very good answer.")
print()

# ---- and the biggest payment out ----------------------------
print("=== ONE MORE, ON THE WAY OUT ===")
dQ1 = df['debit'].quantile(0.25)
dQ3 = df['debit'].quantile(0.75)
dIQR = dQ3 - dQ1
debit_out = df[df['debit'] > dQ3 + 1.5 * dIQR]
print(f"Debits above the fence (${round(dQ3 + 1.5 * dIQR, 2)}):", debit_out.shape[0])
print()
print("Top three:")
print(debit_out.nlargest(3, 'debit')[['date', 'debit', 'counterparty']]
      .to_string(index=False))
print()
print("The branch deposit, and two payroll runs. Every one explainable.")
print("A statement where you can explain every outlier is a statement")
print("a bank can trust.")
