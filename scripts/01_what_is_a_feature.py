# ============================================================
#  The Cozy Bean -- Script 01: What Is a Feature?
#  Lab STEPs 1-2.
#  Shows: the vocabulary, using a table you already know.
#  Run:   python scripts/01_what_is_a_feature.py
#         (from M1-W3-Lab02/)
# ============================================================

import pandas as pd

# A tiny table, typed out by hand, so the words have something
# to point at. Three days of the shop, four facts about each.
days = pd.DataFrame({
    "date":        ["2026-10-29", "2026-10-30", "2026-10-31"],
    "cups_sold":   [138, 152, 161],
    "muffins_sold": [29, 33, 35],
    "takings":     [529.25, 571.40, 604.75],
})

print("=== STEP 1: ROWS AND COLUMNS HAVE PROPER NAMES ===")
print(days)
print()
print("Each ROW is one OBSERVATION -- one day the shop was open.")
print("Each COLUMN is one FEATURE -- one fact about that day.")
print()
print(f"Observations (rows):  {days.shape[0]}")
print(f"Features (columns):   {days.shape[1]}")
print()
print("That is the whole vocabulary. A feature is a column that")
print("tells you something useful. Nothing more mysterious.")
print()

# ---- Section 2  (STEP 2): a feature you MAKE ----------------
print("=== STEP 2: THE FEATURES YOU MAKE YOURSELF ===")
print("Nobody recorded 'takings per cup'. But we can build it:")
print()

days["per_cup"] = (days["takings"] / days["cups_sold"]).round(3)
print(days[["date", "cups_sold", "takings", "per_cup"]])
print()
print("That new column is FEATURE ENGINEERING, and you just did it.")
print("Two columns you had -> one column you did not have, that")
print("answers a question neither of them could answer alone.")
print()
print("It was put like this in class, and it is worth remembering:")
print()
print('    "Better features mean better results."')
print()
print("Better features also mean SIMPLER models -- because a good")
print("feature has already done the hard thinking.")
