# ============================================================
#  The Cozy Bean -- Script 04: Numbers Wearing String Costumes
#  Lab STEP 5 -- the most useful twenty lines in the week.
#  Shows: the four moves that turn text back into money.
#  Run:   python scripts/04_string_surgery.py
#         (from M1-W3-Lab02/)
# ============================================================

import numpy as np
import pandas as pd

df = pd.read_csv("data/cozybean_statement.csv")

# ---- the problem, demonstrated ------------------------------
print("=== BEFORE: what the bank actually sent us ===")
print(df['debit'].head())
print()
print("Ask for the total and pandas does exactly what you said:")
glued = df['debit'].head().sum()
print("  .sum() on that ->", glued)
print("  ...glued end to end, not added up. Because it is TEXT,")
print("  and the way you add text is to stick it together.")
print()

# ---- the four moves ----------------------------------------
# Beat 1: make absolutely sure every cell is text before we do
#         text things to it.
df['debit'] = df['debit'].astype(str)

# Beat 2: strip the thousands separators.
df['debit'] = df['debit'].str.replace(',', '', regex=False)

# Beat 3: turn all three flavours of "nothing" into a real,
#         countable gap.
df['debit'] = df['debit'].replace({'\\N': np.nan,
                                   'None': np.nan,
                                   '': np.nan})

# Beat 4: NOW ask it to be a number.
df['debit'] = pd.to_numeric(df['debit'], errors='coerce')

print("=== AFTER: four small moves later ===")
print(df['debit'].head())
print()
print("  .sum() on that ->", round(df['debit'].head().sum(), 2))
print()
print("Look at the dtype on those two blocks. It went from 'str'")
print("to 'float64'. That one word changing is the whole STEP.")
print()

print("Real gaps we can now count:", int(df['debit'].isna().sum()))
print("Nothing was invented. '\\\\N', 'None' and '' became NaN --")
print("we recorded an absence instead of guessing a value.")
print()

# ---- the other two money columns, same four moves ----------
# A Week-1 for loop, so we write the recipe once.
for col in ['credit', 'closing_balance']:
    df[col] = (df[col]
               .astype(str)
               .str.replace(',', '', regex=False)
               .replace({'\\N': np.nan, 'None': np.nan, '': np.nan}))
    df[col] = pd.to_numeric(df[col], errors='coerce')

print("=== ALL THREE MONEY COLUMNS, DONE ===")
print(df[['debit', 'credit', 'closing_balance']].dtypes)
print()
print("Gaps in each:")
print(df[['debit', 'credit', 'closing_balance']].isna().sum())
print()
print("closing_balance has NO gaps -- the bank always printed a")
print("running balance. It only ever needed its commas removed.")
