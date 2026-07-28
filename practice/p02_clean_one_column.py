# ============================================================
#  PRACTICE p02 -- Clean One Column, Four Moves
#  The Cozy Bean  |  M1-W3 Lab02
#
#  YOUR TASK:
#    STEP 5 cleaned debit and credit. The third money column,
#    closing_balance, is still text. Fix it, with the same four
#    moves, from memory if you can.
#      1. Print its dtype, and one cell that has a comma in it.
#      2. Apply the four moves.
#      3. Print its dtype again, and how many gaps it has.
#      4. Print the lowest, highest and mean balance, with commas
#         and 2 decimal places.
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Before -- dtype: str
#    A cell with a comma in it: '5,176.73'
#    After -- dtype: float64
#    Gaps: 0
#    Lowest balance:  1,615.17
#    Highest balance: 52,076.55
#    Mean balance:    6,581.02
#
#  HINT: The four moves, in order:
#          .astype(str)
#          .str.replace(',', '', regex=False)
#          .replace({'\\N': np.nan, 'None': np.nan, '': np.nan})
#          pd.to_numeric(..., errors='coerce')
#        repr() shows you the quotes around a string.
#        f"{value:,.2f}" gives you commas AND two decimals.
#
#  NOTICE: this column has ZERO gaps. Two of the four moves had
#        nothing to do. Was writing them still worth it?
#
#  How to run it: python practice/p02_clean_one_column.py
#                 (run it from inside the M1-W3-Lab02 folder)
# ============================================================

import numpy as np
import pandas as pd

df = pd.read_csv("data/cozybean_statement.csv")

# TODO 1: dtype before, and a cell with a comma
print("Before -- dtype: (not checked yet)")
print("A cell with a comma in it: (not found yet)")

# TODO 2: the four moves on closing_balance

# TODO 3: dtype after, and the gap count
print("After -- dtype: (not cleaned yet)")
print("Gaps: (not counted yet)")

# TODO 4: lowest, highest, mean -- with commas and 2 decimals
print("Lowest balance:  (not worked out yet)")
print("Highest balance: (not worked out yet)")
print("Mean balance:    (not worked out yet)")
