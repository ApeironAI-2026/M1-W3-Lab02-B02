# ============================================================
#  PRACTICE p01 -- Open the Statement
#  The Cozy Bean  |  M1-W3 Lab02
#
#  YOUR TASK:
#    Before you fix anything, describe what you have been sent.
#      1. How many rows and columns?
#      2. What are the columns called?
#      3. How many loaded as text, and how many as numbers?
#      4. How many different counterparties are in the file?
#      5. What channels appear, in alphabetical order?
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Rows: 1440
#    Columns: 8
#    Column names: ['date', 'debit', 'credit', 'reference', 'closing_balance', 'counterparty_id', 'counterparty', 'channel']
#    How many columns did pandas load as text? 8
#    How many as numbers? 0
#    Counterparties in the file: 13
#    Channels in the file: ['card', 'cash', 'standing_order', 'transfer']
#
#  HINT: list(df.columns) prints the names as a plain list.
#        select_dtypes(include='str') / include='number'.
#        nunique() counts different values; sorted(df[c].unique())
#        gives them alphabetically.
#
#  STOP AND NOTICE: EIGHT text columns and ZERO numeric ones. Not
#        one usable number in a bank statement. And 13 counterparties
#        -- by the end of STEP 6 there will be 12. Why?
#
#  How to run it: python practice/p01_open_the_statement.py
#                 (run it from inside the M1-W3-Lab02 folder)
# ============================================================

import pandas as pd

df = pd.read_csv("data/cozybean_statement.csv")

# TODO 1: rows and columns
print("Rows: (not counted yet)")
print("Columns: (not counted yet)")

# TODO 2: the column names as a list
print("Column names: (not listed yet)")

# TODO 3: how many text, how many numeric
print("How many columns did pandas load as text? (not counted yet)")
print("How many as numbers? (not counted yet)")

# TODO 4: how many counterparties
print("Counterparties in the file: (not counted yet)")

# TODO 5: the channels, alphabetically
print("Channels in the file: (not listed yet)")
