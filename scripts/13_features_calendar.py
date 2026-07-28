# ============================================================
#  The Cozy Bean -- Script 13: The Features That Need a Calendar
#  Lab STEP 16.
#  Shows: three more features, all built out of the date column.
#  Run:   python scripts/13_features_calendar.py
#         (from M1-W3-Lab02/)
# ============================================================

import numpy as np
import pandas as pd

# The date the bank will look at this pack. Everything "recent"
# is measured against THIS, not against the data itself -- see
# the note at the bottom of this script for why that matters.
REVIEW_DATE = pd.Timestamp("2026-11-06")

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

# ---- Feature 6: how many different days ---------------------
print("=== FEATURE 6 -- HOW MANY DIFFERENT DAYS? ===")
activity = (
    df.groupby('counterparty_id', as_index=False)
      .agg(active_days=('date', 'nunique'))
)
print(activity.to_string(index=False))
print()
print("'nunique' counts DIFFERENT values. Five transactions on one")
print("day is one active day. This is a rhythm, not a total.")
print()

# ---- Feature 7: the busiest day of the week -----------------
print("=== FEATURE 7 -- WHICH DAY OF THE WEEK? ===")
df['day_name'] = df['date'].dt.day_name()
print("A whole new column, out of thin air:")
print(df[['date', 'day_name', 'counterparty']].head(3).to_string(index=False))
print()
print("Across the whole statement, our busiest weekday is:")
print(df['day_name'].value_counts())
print()

# Per counterparty. A Week-1 for loop over the groups, because
# 'the commonest value in this group' is easiest to read that way.
rows = []
for cp_id, group in df.groupby('counterparty_id'):
    day_counts = group['day_name'].value_counts()
    rows.append({
        'counterparty_id': cp_id,
        'busiest_day': day_counts.idxmax(),
    })
busiest = pd.DataFrame(rows)

print("And per counterparty:")
print(busiest.to_string(index=False))
print()
print(".idxmax() means 'the label with the biggest count' -- the")
print("winner's NAME, not the number of times it won.")
print()

# ---- Feature 8: how long since we last heard from them ------
print("=== FEATURE 8 -- HOW RECENTLY? ===")
recency = (
    df.groupby('counterparty_id', as_index=False)
      .agg(last_txn_date=('date', 'max'))
)
recency['days_since_last_txn'] = (REVIEW_DATE - recency['last_txn_date']).dt.days

print(f"Measuring everything against the review date: {REVIEW_DATE.date()}")
print()
print(recency.to_string(index=False))
print()

# ---- the trap, explained ------------------------------------
print("=== WHY THE REFERENCE DATE HAS TO COME FROM OUTSIDE ===")
print("Suppose we had measured 'days since last transaction' against")
print("each counterparty's OWN last transaction. Watch what happens:")
print()
broken = (recency['last_txn_date'] - recency['last_txn_date']).dt.days
print("  days_since_last_txn would be:", broken.unique().tolist())
print()
print("Zero. Every time. For everybody. Because you asked how long")
print("it has been since the last day... measured from the last day.")
print()
print("The class notebook has exactly this bug, and its version of")
print("this feature reads 0 for every single customer. A feature that")
print("is the same for every row tells a model NOTHING.")
print()
print("So a recency feature always needs a fixed outside date:")
print("today, the application date, or -- as here -- the review date.")
