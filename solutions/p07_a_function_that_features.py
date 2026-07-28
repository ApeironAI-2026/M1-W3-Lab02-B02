# ============================================================
#  SOLUTION p07 -- The Function That Ends the Copy-Pasting
#  The Cozy Bean  |  M1-W3 Lab02
#
#  How to run it: python solutions/p07_a_function_that_features.py
#                 (run it from inside the M1-W3-Lab02 folder)
# ============================================================

import numpy as np
import pandas as pd


def load_clean_statement(path):
    """Read the statement and do every cleaning move from STEPs 4-6."""
    df = pd.read_csv(path)

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
    return df


def build_features(df):
    """One row per counterparty, four features each."""
    features = (
        df.groupby('counterparty_id', as_index=False)
          .agg(counterparty=('counterparty', 'first'),
               total_debit=('debit', 'sum'),
               total_credit=('credit', 'sum'),
               txn_count=('reference', 'count'))
    )
    features['net_position'] = (features['total_credit']
                                - features['total_debit'])
    return features


statement = load_clean_statement("data/cozybean_statement.csv")
print("Clean rows:", statement.shape[0])

table = build_features(statement)
print("Feature table shape:", table.shape)
print(table.round(2).to_string(index=False))

biggest = table.nlargest(1, 'net_position').iloc[0]
print(f"Best net position: {biggest['counterparty']} "
      f"({biggest['net_position']:,.2f})")

# Nine lines of cleaning, written ONCE. Every script in this lab's
# scripts/ folder repeats that block by hand, on purpose, so that
# each one runs standalone -- and so that by the time you got here
# you were thoroughly sick of typing it. That irritation is the
# lesson: repetition is the signal that a function is missing.
