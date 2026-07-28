# ============================================================
#  The Cozy Bean -- Script 11: Putting Columns on One Ruler
#  Lab STEP 13.
#  Shows: min-max scaling and z-score standardisation, both
#         worked out with plain Week-1 arithmetic.
#  Run:   python scripts/11_scaling_by_hand.py
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

payments = df.loc[df['debit'] > 0, 'debit']

print("=== STEP 13: WHY SCALE ANYTHING? ===")
print("Two of our columns, side by side:")
print(f"  debit           runs from {payments.min():>10,.2f} to {payments.max():>12,.2f}")
print(f"  closing_balance runs from {df['closing_balance'].min():>10,.2f} "
      f"to {df['closing_balance'].max():>12,.2f}")
print()
print("Same units, wildly different ranges. Some algorithms treat a")
print("bigger number as a more important number, purely because it")
print("is bigger. Scaling stops that.")
print()

# ---- Min-max: squeeze everything into 0..1 ------------------
print("=== NORMALISATION (MIN-MAX): PUT EVERYTHING IN 0 TO 1 ===")
print("    scaled = (x - min) / (max - min)")
print()

lo = payments.min()
hi = payments.max()
minmax = (payments - lo) / (hi - lo)

print(f"min = {lo}")
print(f"max = {hi:,.2f}")
print()
print("First five payments, before and after:")
compare = pd.DataFrame({'original': payments.head(),
                        'min_max': minmax.head().round(6)})
print(compare)
print()
print(f"Smallest becomes exactly {minmax.min():.1f}, largest exactly {minmax.max():.1f}.")
print("Every other payment lands somewhere in between. That is all it does.")
print()

# ---- Z-score: centre on 0, measure in std devs --------------
print("=== STANDARDISATION (Z-SCORE): CENTRE ON ZERO ===")
print("    scaled = (x - mean) / std")
print()

mean = payments.mean()
std = payments.std()
zscores = (payments - mean) / std

print(f"mean = {mean:,.6f}")
print(f"std  = {std:,.6f}")
print()
print("First five payments, before and after:")
compare2 = pd.DataFrame({'original': payments.head(),
                         'z_score': zscores.head().round(6)})
print(compare2)
print()
print(f"New mean: {zscores.mean():.6f}   new std: {zscores.std():.6f}")
print("Centred on zero, one standard deviation wide. By construction.")
print()

print("=== YOU HAVE ALREADY DONE THIS ===")
print("Look at that second formula again:  (x - mean) / std")
print()
print("That is EXACTLY the z-score you worked out by hand for one")
print("late flight in Lab01 STEP 14. Same arithmetic, same two")
print("ingredients. There it was a way to spot a weird value. Here")
print("it is a way to prepare a column for a model.")
print()
print("One formula, two jobs. Week-1 arithmetic IS ML preprocessing.")
print()
print("Who cares about this? K-means, linear regression and neural")
print("networks all behave badly on unscaled columns. Names only")
print("for now -- you meet them in Module 2.")
