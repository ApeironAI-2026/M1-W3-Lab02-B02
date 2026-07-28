# ============================================================
#  The Cozy Bean -- Script 10: Words a Model Can Read
#  Lab STEP 12.
#  Shows: one-hot encoding -- one text column becoming several
#         columns of 0s and 1s.
#  Run:   python scripts/10_one_hot_channel.py
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

# ---- the column we are going to convert ---------------------
print("=== STEP 12: THE COLUMN THAT IS STILL WORDS ===")
print("How did the money move?")
print(df['channel'].value_counts())
print()
print("Four values, all text. A model cannot add up the word")
print("'transfer'. So we turn one text column into several")
print("number columns -- one per value, each answering yes or no.")
print()

# ---- one line does it ---------------------------------------
dummies = pd.get_dummies(df['channel'], prefix='channel')

print("=== ONE LINE LATER ===")
print("New columns:", list(dummies.columns))
print()
print("pandas hands them to you as True/False:")
print(dummies.head())
print()

# Class describes 'binary (0/1) features', so make them so.
dummies = dummies.astype(int)
print("...and .astype(int) turns those into the 0s and 1s your")
print("class describes. Same information, easier to read:")
print(dummies.head())
print()

# ---- read one row out loud ----------------------------------
print("=== READ ROW 2 OUT LOUD ===")
row = dummies.iloc[2]
original = df['channel'].iloc[2]
print(f"The original value was: '{original}'")
print(row.to_string())
print()
print(f"In English: 'this transaction was NOT card, NOT cash,")
print(f"NOT a standing order, and YES a {original}.'")
print("Exactly one 1 per row. That is why it is called ONE-hot.")
print()

# ---- staple them on -----------------------------------------
df = pd.concat([df, dummies], axis=1)
print("=== THE COST, STATED PLAINLY ===")
print("Columns before encoding: 9")
print("Columns after encoding: ", df.shape[1])
print()
print("Four new columns for four values. That is fine. But imagine")
print("one-hot encoding a column with 500 counterparty names --")
print("you would get 500 columns. That is the trade-off, and it is")
print("why you encode the small columns and think hard about the big ones.")
