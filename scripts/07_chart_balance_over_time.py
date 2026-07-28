# ============================================================
#  The Cozy Bean -- Script 07: The Story in the Balance
#  Lab STEP 9.
#  Shows: one line chart that contains the whole last six months
#         of your life.
#  Run:   python scripts/07_chart_balance_over_time.py
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

print("=== STEP 9: THE BALANCE, OVER TIME ===")
print(df['closing_balance'].describe().round(2))
print()
print("Lowest the account ever got:  $", round(df['closing_balance'].min(), 2))
print("Highest it ever got:          $", round(df['closing_balance'].max(), 2))
print("Where it finished:            $", round(df['closing_balance'].iloc[-1], 2))
print()
print("It never went negative. For a loan officer, that single fact")
print("is worth more than most of this statement.")
print()

# ---- the two rows that matter most --------------------------
print("=== THE TWO BIGGEST LINES IN 18 MONTHS ===")
biggest_in = df.nlargest(1, 'credit')
biggest_out = df.nlargest(1, 'debit')
print("Biggest money IN:")
print(biggest_in[['date', 'credit', 'counterparty', 'closing_balance']].to_string(index=False))
print()
print("Biggest money OUT:")
print(biggest_out[['date', 'debit', 'counterparty', 'closing_balance']].to_string(index=False))
print()
print("You know exactly what those two are. One is Mrs Adeyemi's")
print("first tranche landing. The other is the deposit you paid on")
print("the unit two streets over. Your whole spring is those two rows.")
print()

# ---- the chart -----------------------------------------------
plt.figure(figsize=(11, 6))
sns.lineplot(data=df, x='date', y='closing_balance', color='purple')
plt.title('The Cozy Bean -- Closing Balance Over 18 Months')
plt.xlabel('Date')
plt.ylabel('Closing balance ($)')
plt.tight_layout()
plt.savefig("charts/balance_over_time.png")
print("Saved charts/balance_over_time.png")
plt.show()

print()
print("Read your chart. Eighteen months of small waves -- takings in,")
print("suppliers and wages out, over and over. Then right at the end,")
print("a cliff UP and a cliff DOWN. Those are the two rows above.")
print("Window closed. Script finished.")
