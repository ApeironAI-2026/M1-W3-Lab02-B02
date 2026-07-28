# ============================================================
#  The Cozy Bean -- Script 05: Fill the Gaps, Drop the Nothings
#  Lab STEPs 6-7.
#  Shows: filling the gaps with a real decision behind it, the
#         ~ (NOT) operator, and the imputation rules.
#  Run:   python scripts/05_fill_and_filter.py
#         (from M1-W3-Lab02/)
# ============================================================

import numpy as np
import pandas as pd

df = pd.read_csv("data/cozybean_statement.csv")

# Pick up where STEP 5 left off. A Week-1 for loop over the three
# money columns, so we write the recipe once instead of three times.
for col in ['debit', 'credit', 'closing_balance']:
    df[col] = (df[col]
               .astype(str)
               .str.replace(',', '', regex=False)
               .replace({'\\N': np.nan, 'None': np.nan, '': np.nan}))
    df[col] = pd.to_numeric(df[col], errors='coerce')

# ---- Section 1  (STEP 6a): fill, with a reason ---------------
print("=== STEP 6: WHAT DOES A GAP IN 'DEBIT' ACTUALLY MEAN? ===")
print("Gaps before filling:")
print(df[['debit', 'credit']].isna().sum())
print()
print("Think about what the gap MEANS here. Every line of a bank")
print("statement is money in OR money out, never both. A gap in")
print("'debit' does not mean 'we do not know'. It means ZERO --")
print("no money went out on that line, because money came IN.")
print()
print("That is why 0.0 is the honest fill here, and why a median")
print("or a mean would be nonsense.")
print()

df = df.fillna({'debit': 0.0, 'credit': 0.0})
print("Gaps after filling:")
print(df[['debit', 'credit']].isna().sum())
print()

# ---- Section 2  (STEP 6b): the ~ operator -------------------
print("=== STEP 6: THE ROWS WHERE NOTHING HAPPENED ===")
nothing = (df['credit'] == 0) & (df['debit'] == 0)
print("Rows with zero on BOTH sides:", int(nothing.sum()))
print()
print("These are the bank's own memo lines -- 'balance brought")
print("forward' and the like. Real rows, no money. They would drag")
print("every average we calculate towards zero.")
print()
print("Meet a new operator. In Week 2 you learned & for AND and")
print("| for OR. The third one is ~ for NOT:")
print()
print("    df[~((df['credit'] == 0) & (df['debit'] == 0))]")
print("       ^ keep the rows where this is NOT true")
print()

before = df.shape[0]
df = df[~((df['credit'] == 0) & (df['debit'] == 0))]
print(f"Rows before: {before}   after: {df.shape[0]}")
print()
print("And a way to check we removed the right thing -- those memo")
print("lines were the only ones tagged c0:")
print("Rows still tagged c0:", int((df['counterparty_id'] == 'c0').sum()))
print("Counterparties left: ", df['counterparty_id'].nunique())
print()

# ---- Section 3  (STEP 7): the imputation rule set ------------
print("=== STEP 7: THE RULES, FOR NEXT TIME ===")
print("A rule was given in class for each kind of column:")
print()
print("  NUMERIC column     -> fill with the mean or the median")
print("                        (median when the data is skewed --")
print("                         which money always is)")
print("  CATEGORICAL column -> fill with the mode, the commonest")
print("                        value, or the label 'Missing'")
print()
print("The goal: keep your data size without inventing signal.")
print("And the exception we just used: when a gap has a MEANING,")
print("use the meaning. Here the meaning was zero.")
print()
print("When would you rather drop? When the row is too damaged to")
print("trust -- like the six mangled dates in STEP 4.")
