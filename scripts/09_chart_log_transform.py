# ============================================================
#  The Cozy Bean -- Script 09: Squash the Giants
#  Lab STEP 11.
#  Shows: the log transform, why you must filter first, and the
#         before/after histograms side by side.
#  Run:   python scripts/09_chart_log_transform.py
#         (from M1-W3-Lab02/)
# ============================================================

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("charts", exist_ok=True)

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

# ---- why we cannot just log the column ----------------------
print("=== STEP 11: THE ZERO PROBLEM ===")
zeros = (df['debit'] == 0).sum()
print(f"Rows where debit is exactly 0.00: {zeros} of {df.shape[0]}")
print()
print("Those are the money-IN rows -- nothing went out, so debit is")
print("zero. And you cannot take the logarithm of zero. There is no")
print("power you can raise 10 to and get 0.")
print()
print("Ask numpy anyway and it warns you, then hands back -inf,")
print("which poisons every chart it touches. So we filter first.")
print()

# ---- filter to the rows where money actually moved ----------
# Week-2 boolean filtering, doing something important.
payments = df.loc[df['debit'] > 0, 'debit']

print("=== ONLY THE ROWS WHERE MONEY ACTUALLY MOVED ===")
print(f"Real payments out: {len(payments)}")
print(payments.describe().round(2))
print()

logged = np.log(payments)

print("=== THE SAME PAYMENTS, LOGGED ===")
print(logged.describe().round(4))
print()
print("Before: smallest $%.2f, biggest $%.2f -- a %.0fx spread."
      % (payments.min(), payments.max(), payments.max() / payments.min()))
print("After:  smallest %.2f, biggest %.2f -- a %.1fx spread."
      % (logged.min(), logged.max(), logged.max() / logged.min()))
print()
print("Nothing was deleted and no order changed. The biggest payment")
print("is still the biggest. We just stopped it shouting.")
print()

# ---- before and after, side by side -------------------------
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.histplot(payments, kde=True, color='tomato')
plt.title('Payments out -- as they are')
plt.xlabel('Amount ($)')

plt.subplot(1, 2, 2)
sns.histplot(logged, kde=True, color='seagreen')
plt.title('Payments out -- logged')
plt.xlabel('log(amount)')

plt.tight_layout()
plt.savefig("charts/log_transform.png")
print("Saved charts/log_transform.png")
plt.show()

print()
print("Left: one tall bar at the far left, empty space, a speck.")
print("Right: an actual shape you can read. Same payments, both times.")
print("THAT is what the log transform is for.")
print("Window closed. Script finished.")
