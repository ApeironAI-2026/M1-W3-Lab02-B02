# ============================================================
#  The Cozy Bean -- Script 06: The Shape of the Money
#  Lab STEP 8.
#  Shows: two histograms side by side, and a two-column boxplot.
#  Run:   python scripts/06_chart_money_distributions.py
#         (from M1-W3-Lab02/)
# ============================================================

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("charts", exist_ok=True)

df = pd.read_csv("data/cozybean_statement.csv")

# Pick up where STEPs 5-6 left off. (Practice p07 turns this
# whole block into a function, which is where it belongs.)
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

print("=== STEP 8: THE SHAPE OF THE MONEY ===")
print(df[['debit', 'credit']].describe().round(2))
print()
print("Read the debit column: the middle payment is tiny, the mean")
print("is several times bigger, and the max is enormous. That gap")
print("between the middle and the mean is SKEW, and money data")
print("always has it -- a few big payments drag the average up.")
print()

# ---- two histograms, side by side ---------------------------
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.histplot(df['debit'], kde=True, color='blue')
plt.title('Money Out (debit)')
plt.xlabel('Amount ($)')

plt.subplot(1, 2, 2)
sns.histplot(df['credit'], kde=True, color='green')
plt.title('Money In (credit)')
plt.xlabel('Amount ($)')

plt.tight_layout()
plt.savefig("charts/money_distributions.png")
print("Saved charts/money_distributions.png")
plt.show()

# ---- and both columns in one boxplot ------------------------
plt.figure(figsize=(8, 6))
sns.boxplot(data=df[['debit', 'credit']])
plt.title('The Cozy Bean -- Debit and Credit side by side')
plt.ylabel('Amount ($)')
plt.tight_layout()
plt.savefig("charts/money_boxplot.png")
print("Saved charts/money_boxplot.png")
plt.show()

print()
print("Both charts are almost unreadable -- everything is squashed")
print("into a stripe at the bottom with a few dots far above.")
print("That is not a broken chart. That is what skew LOOKS like,")
print("and STEP 11 has the fix.")
print("Window closed. Script finished.")
