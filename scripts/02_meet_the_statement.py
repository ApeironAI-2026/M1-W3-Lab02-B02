# ============================================================
#  The Cozy Bean -- Script 02: Meet the Statement
#  Lab STEP 3.
#  Shows: what the bank actually sent us, and why it is a mess.
#  Run:   python scripts/02_meet_the_statement.py
#         (from M1-W3-Lab02/)
# ============================================================

import pandas as pd

df = pd.read_csv("data/cozybean_statement.csv")

print("=== STEP 3: 18 MONTHS OF THE COZY BEAN'S BANK ACCOUNT ===")
print("Shape (rows, columns):", df.shape)
print()

print("The first five lines:")
print(df[['date', 'debit', 'credit', 'closing_balance', 'counterparty']].head())
print()

print("=== THE INVENTORY ===")
df.info()
print()

print("=== NOW LOOK AGAIN, AND BE HORRIFIED ===")
print("Every single column says 'str'. Every one. Including the money.")
print()
print("Some actual cells from the debit column:")
print(df['debit'].head(12).to_list())
print()
print("Read that list slowly. FIVE different things are wrong:")
print("  '304.71'    a number... stored as text")
print("  '1,850.00'  a number with a COMMA in it")
print("  '0.00'      a real zero, which we will have to think about")
print("  '\\\\N'        a database's way of writing 'nothing here'")
print("  'None'      a Python word that leaked into the file")
print()
print("And one thing that is already half-fixed: that bare 'nan' in")
print("the list. Some cells in the file are genuinely empty, and")
print("read_csv is kind enough to turn those into NaN for us on the")
print("way in. The other three flavours of 'nothing' it left alone,")
print("because as far as it can tell they are ordinary words.")
print()

print("And the dates are text too:")
print(df['date'].head(3).to_list())
print()

print("What we have got, in one sentence: 1,440 rows of evidence")
print("for a loan application, and not one usable number in sight.")
print("STEPs 4 to 9 fix that. Then the real work starts.")
