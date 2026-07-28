# ============================================================
#  PRACTICE p05 -- One-Hot the Channel Column
#  The Cozy Bean  |  M1-W3 Lab02
#
#  YOUR TASK:
#    Encode the channel column, then CHECK your own work -- which
#    is the part people skip.
#      1. List the channel values and how many of each.
#      2. One-hot encode the column, as 0s and 1s (not True/False).
#      3. Print the new column names and the shape.
#      4. Show the first three rows.
#      5. PROVE every row has exactly one 1 in it.
#      6. PROVE the column totals match the counts from step 1.
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Channel values: ['card', 'cash', 'standing_order', 'transfer']
#    How many of each:
#    channel
#    transfer          741
#    card              567
#    standing_order     78
#    cash               54
#    Name: count, dtype: int64
#    New columns: ['channel_card', 'channel_cash', 'channel_standing_order', 'channel_transfer']
#    Shape of the encoded block: (1440, 4)
#    First three rows:
#       channel_card  channel_cash  channel_standing_order  channel_transfer
#    0             1             0                       0                 0
#    1             0             1                       0                 0
#    2             0             0                       0                 1
#    Rows whose 0/1 columns add up to exactly 1: 1440 of 1440
#    Column totals match the original counts:
#    channel_card              567
#    channel_cash               54
#    channel_standing_order     78
#    channel_transfer          741
#    dtype: int64
#
#  HINT: pd.get_dummies(df['channel'], prefix='channel').astype(int)
#        encoded.sum(axis=1) adds ACROSS each row -- that is the
#        one-hot check. encoded.sum() adds DOWN each column.
#        axis=1 means "across the row"; no axis means "down the column".
#
#  WHY CHECK AT ALL? Because encoding silently changes the shape of
#        your data, and a silent change is the kind you find out
#        about three steps later.
#
#  How to run it: python practice/p05_one_hot_the_channel.py
#                 (run it from inside the M1-W3-Lab02 folder)
# ============================================================

import pandas as pd

df = pd.read_csv("data/cozybean_statement.csv")

# TODO 1: the channel values and their counts
print("Channel values: (not listed yet)")
print("How many of each:")
print("(not counted yet)")

# TODO 2 and 3: encode as 0/1, then names and shape
print("New columns: (not encoded yet)")
print("Shape of the encoded block: (not encoded yet)")

# TODO 4: first three rows
print("First three rows:")
print("(not encoded yet)")

# TODO 5: prove exactly one 1 per row
print("Rows whose 0/1 columns add up to exactly 1: (not checked yet)")

# TODO 6: prove the column totals match
print("Column totals match the original counts:")
print("(not checked yet)")
