# 📋 Lab02 Cheat Sheet — The Cleaning & Feature Recipes

**The Cozy Bean · M1-W3-Lab02 · Apeiron AI Training Academy**

*Print this one. The four-move chain alone will save you a hundred hours.*

---

## ⭐ THE FOUR-MOVE STRING CHAIN

**When a money column arrives as text.** This is the single most reusable thing in the week.

```python
import numpy as np
import pandas as pd

df['debit'] = df['debit'].astype(str)                              # 1
df['debit'] = df['debit'].str.replace(',', '', regex=False)         # 2
df['debit'] = df['debit'].replace({'\\N': np.nan,                   # 3
                                   'None': np.nan,
                                   '': np.nan})
df['debit'] = pd.to_numeric(df['debit'], errors='coerce')           # 4
```

| Beat | What it does | Why it is there |
|---|---|---|
| **1** `.astype(str)` | force the column to text | `.str` only works on text. **Skip it and you get `AttributeError`** |
| **2** `.str.replace(',', '', regex=False)` | strip thousands separators | `1,850.00` cannot become a number while the comma is there |
| **3** `.replace({...})` | turn "nothing" markers into real gaps | **no `.str`** — this swaps whole *values*, not pieces of text |
| **4** `pd.to_numeric(errors='coerce')` | finally, be a number | anything still unreadable becomes `NaN` rather than crashing |

**All three money columns at once, with a Week-1 loop:**

```python
for col in ['debit', 'credit', 'closing_balance']:
    df[col] = (df[col]
               .astype(str)
               .str.replace(',', '', regex=False)
               .replace({'\\N': np.nan, 'None': np.nan, '': np.nan}))
    df[col] = pd.to_numeric(df[col], errors='coerce')
```

> ### ⚠️ The most dangerous bug in the week
>
> **Skip beat 2 and nothing crashes.** `pd.to_numeric` cannot read `1,850.00`, so `errors='coerce'` silently turns **your biggest values** into `NaN`. Every total afterwards is too small and nothing says so.
>
> **After any cleaning chain, check `df[col].isna().sum()`** against what you expected.

**`read_csv` already handles truly blank cells** (they arrive as `NaN`). It leaves `\N` and `None` alone, because they look like ordinary words.

---

## ⭐ THE FULL CLEANING BLOCK

The nine lines every analysis of this statement begins with:

```python
df = pd.read_csv("data/cozybean_statement.csv")

for col in ['debit', 'credit', 'closing_balance']:
    df[col] = (df[col].astype(str)
               .str.replace(',', '', regex=False)
               .replace({'\\N': np.nan, 'None': np.nan, '': np.nan}))
    df[col] = pd.to_numeric(df[col], errors='coerce')

df['date'] = pd.to_datetime(df['date'], errors='coerce')
df = df.dropna(subset=['date'])
df = df.fillna({'debit': 0.0, 'credit': 0.0})
df = df[~((df['credit'] == 0) & (df['debit'] == 0))]
```

**Typed it more than twice? Make it a function.** That is practice p07:

```python
def load_clean_statement(path):
    ...
    return df
```

---

## Dates, forgivingly

```python
df['date'] = pd.to_datetime(df['date'], errors='coerce')   # unreadable -> NaT
print(df['date'].isna().sum())                             # ALWAYS count them
df = df.dropna(subset=['date'])                            # then decide
```

**`errors='coerce'` = "if you cannot read it, write `NaT` and carry on."** It fails **silently** — that is the point of it, and it is why the `isna().sum()` on the next line is not optional.

`NaT` is "Not a Time" — the date version of `NaN`.

**Watch for dates with good posture:** `31/02/2026` *looks* like a date but February has no 31st. `coerce` catches it without knowing anything about calendars.

---

## Imputation — filling gaps

| Column type | Fill with | Why |
|---|---|---|
| **Numeric** | mean or **median** | median when skewed — and **money is always skewed** |
| **Categorical** | the **mode**, or a label like `"Missing"` | you cannot average a word |

```python
df = df.fillna({'debit': 0.0, 'credit': 0.0})    # a dict: one value per column
df['c'] = df['c'].fillna(df['c'].median())
df['ch'] = df['ch'].fillna(df['ch'].mode()[0])   # mode() returns a Series
```

**Goal:** keep your data size without inventing signal.

> ## Fill from MEANING, not from habit.
>
> On a bank statement, a gap in `debit` does not mean *"we do not know"*. Every line is money in **or** out. It means **zero**.
>
> A median of \$70 dropped into 565 money-in rows would invent \$40,000 of payments that never happened.

**Drop instead when the row is too damaged to trust** — a transaction with no date.

**And remember:** every imputed value afterwards looks exactly like data. Nothing marks it.

---

## `~` — the NOT operator

| Week 1 (single answers) | pandas (whole columns) |
|---|---|
| `and` | `&` |
| `or` | `\|` |
| **`not`** | **`~`** |

```python
df = df[~((df['credit'] == 0) & (df['debit'] == 0))]
#        ^ keep the rows where this is NOT true
```

**Bracket the whole condition.** `df[~(df['a'] == 0) & (df['b'] == 0)]` applies `~` to only the first part and means something completely different — and it runs without complaint.

**The same filter without `~`:** `df[(df['credit'] != 0) | (df['debit'] != 0)]`. *"NOT (both zero)"* = *"either one is not zero"*.

**Verify a filter properly.** Do not just check the row count dropped — check the thing you meant to remove is gone and nothing else went with it:

```python
print("rows:", before, "->", df.shape[0])
print("target rows left:", (df['counterparty_id'] == 'c0').sum())   # want 0
print("groups left:", df['counterparty_id'].nunique())
```

---

## ⭐ LOG TRANSFORM — and the guard

```python
payments = df.loc[df['debit'] > 0, 'debit']    # FILTER FIRST
logged = np.log(payments)
```

**You cannot take the log of zero.** Unguarded you get:

```text
RuntimeWarning: divide by zero encountered in log
min: -inf     mean: -inf
```

**`-inf` is not a small number, it is a broken one, and it spreads** — into your min, your mean, and any chart it touches.

**One plain sentence for why:** *you cannot log zero, so we log only the rows where money actually moved.*

**What it does:** compresses large values far more than small ones. A 633× spread becomes 2.7×. **Nothing is deleted and no order changes** — the biggest payment is still the biggest, it just stops shouting.

**The alternative** (🚀 bonus): `np.log1p(x)` computes `log(1 + x)`, so zero gives `0.0` — no filter needed. But it treats "no payment" and "a \$0 payment" as the same thing. **Both are defensible; know which question you asked.**

---

## ⭐ ONE-HOT ENCODING

```python
dummies = pd.get_dummies(df['channel'], prefix='channel')
dummies = dummies.astype(int)          # True/False -> 1/0
df = pd.concat([df, dummies], axis=1)
```

One text column → **several 0/1 columns, one per value, exactly one `1` per row.** That is where "one-hot" comes from.

**Read a row aloud:** *"not card, not cash, not a standing order, and YES a transfer."*

**Check your work:**

```python
dummies.sum(axis=1)     # across each row -- must ALL be 1
dummies.sum()           # down each column -- must match value_counts()
```

**The cost is columns.** 4 values → 4 columns, fine. A column with 500 names → **500 columns**, mostly zeros. **Encode the small categoricals; think hard about the big ones.**

**Do not one-hot an identifier.** IDs are labels, not categories.

---

## ⭐ SCALING — two rulers

```python
# Normalisation (min-max): squeeze into 0...1
scaled = (col - col.min()) / (col.max() - col.min())

# Standardisation (z-score): centre on 0, one std wide
scaled = (col - col.mean()) / col.std()
```

| | Always gives | Says | Use when |
|---|---|---|---|
| **Min-max** | exactly 0.0 and 1.0 at the ends | *"this was the largest one"* | you need a guaranteed range |
| **Z-score** | mean 0, std 1 | *"this is 8 standard deviations out"* | you care how **unusual** a value is |

> ### 🔙 That z-score formula is the SAME one you used to find outliers.
>
> `(x - mean) / std` — in Lab01 it spotted a weird flight. Here it prepares a column for a model. **One formula, two jobs.**

**Who cares:** K-means, linear regression, neural networks. *(Tree-based methods largely do not.)*

**Watch out for `data leakage`** — scaling with the whole dataset's statistics before splitting into train and test sets leaks information. Not a today problem, but know the phrase.

---

## ⭐ NAMED AGGREGATIONS — building features

```python
totals = (
    df.groupby('counterparty_id', as_index=False)
      .agg(
          total_debit=('debit', 'sum'),
          total_credit=('credit', 'sum'),
          mean_debit=('debit', 'mean'),
          txn_count=('reference', 'count'),
          active_days=('date', 'nunique'),
          last_txn_date=('date', 'max'),
          counterparty=('counterparty', 'first'),
      )
)
```

```text
total_debit = ('debit', 'sum')
     ^            ^        ^
new column    old column  what to do
```

**Flat, properly-named columns** — no two-level headers to flatten. Prefer this over `agg({'col': ['sum', 'mean']})`.

`as_index=False` keeps the grouping column as a normal column.

| Aggregation | Gives |
|---|---|
| `'sum'`, `'mean'`, `'min'`, `'max'`, `'std'` | the obvious |
| `'count'` | number of **non-null** values in the pile |
| `'nunique'` | number of **different** values |
| `'first'`, `'last'` | first/last in the pile |

> ⚠️ **`'count'` counts rows that have a value, not rows you find interesting.** After `fillna(0)` the zeros count too. For real payments: `(df['debit'] > 0).sum()`.

**Some features need no groupby at all** — just arithmetic:

```python
totals['net_position'] = totals['total_credit'] - totals['total_debit']
```

---

## Calendar features

```python
df['day_name'] = df['date'].dt.day_name()          # 'Monday'
df['month'] = df['date'].dt.to_period('M').astype(str)   # '2026-10'
```

**Commonest value per group** — a Week-1 loop, no lambda needed:

```python
rows = []
for key, group in df.groupby('counterparty_id'):
    rows.append({'counterparty_id': key,
                 'busiest_day': group['day_name'].value_counts().idxmax()})
busiest = pd.DataFrame(rows)
```

**`.idxmax()` gives the label with the biggest count** — the winner's *name*, not its count.

### Recency — and the trap

```python
REVIEW_DATE = pd.Timestamp("2026-11-06")          # from OUTSIDE the data

recency = df.groupby('id', as_index=False).agg(last_txn=('date', 'max'))
recency['days_since'] = (REVIEW_DATE - recency['last_txn']).dt.days
```

> ## ⚠️ Never measure recency against the group's own maximum date.
>
> ```python
> today = group['date'].max()
> last  = group['date'].max()      # the same thing
> days  = (today - last).days      # ALWAYS 0. For everybody.
> ```
>
> **A feature with the same value in every row carries no information.** It is a column of zeros with a useful-sounding name.
>
> **Always sanity-check a new feature:** `df['my_feature'].nunique()`. If it is 1, you have not built a feature.

Subtracting dates gives a **Timedelta**. **`.dt.days`** turns it into a number.

---

## ⭐ MERGE — stapling tables on a key

```python
merged = pd.merge(left_table, right_table, on='counterparty_id', how='left')
```

- **`on=`** the **key** — a column present in both tables
- **`how='left'`** — **keep every row from the LEFT table**, bring over matches from the right

| `how=` | Keeps |
|---|---|
| `'left'` | every row from the left; `NaN` where the right has no match |
| `'inner'` | **only** rows present in both — **rows can vanish** |
| `'outer'` | every row from both |

> ## Always check after a merge. Always.
>
> ```python
> print(merged.shape)                 # did the ROW COUNT change unexpectedly?
> print(merged.isna().sum())          # did the merge introduce NEW gaps?
> ```
>
> **A merge that fails to match is silent.** Row count looks right, columns look right, a third of your values are `NaN` because the key had trailing spaces in one table.
>
> **And a non-unique key on the right DUPLICATES rows** — your 12-row table quietly becomes 13, inflating every total afterwards.

---

## Money distributions

```python
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)                 # 1 row, 2 cols, this is chart 1
sns.histplot(df['debit'], kde=True, color='blue')

plt.subplot(1, 2, 2)                 # ...chart 2
sns.histplot(df['credit'], kde=True, color='green')

plt.tight_layout()
plt.savefig("charts/money.png")
plt.show()

plt.figure()                          # NEW figure, or you draw on top
sns.boxplot(data=df[['debit', 'credit']])
sns.lineplot(data=df, x='date', y='closing_balance')
```

**mean ≫ median = skew.** Money always has it. A squashed, unreadable histogram is not a broken chart — it is what skew looks like.

---

## Outliers on your own money

```python
Q1, Q3 = df['credit'].quantile(0.25), df['credit'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['credit'] < Q1 - 1.5*IQR) | (df['credit'] > Q3 + 1.5*IQR)]
```

**Flag, don't delete:**

```python
df['flagged'] = False
df.loc[outliers.index, 'flagged'] = True
df['flag_reason'] = ""
df.loc[outliers.index, 'flag_reason'] = "large credit - loan tranche, expected"
```

> **An outlier is a question, not a verdict.** If the biggest outlier in your file is the loan the bank just gave you, deleting it destroys your own evidence.
>
> **A statement where you can explain every outlier is a statement a bank can trust.**

**`Q1 = 0.0` is not an error** if more than a quarter of the column is zeros. The formula does not know your column is half zeros. You do.

---

## Shipping the evidence pack

```python
features.to_csv("engineered_counterparties.csv", index=False)

lines = []
lines.append(f"Money in:  ${money_in:>12,.2f}")
lines.append(f"  {name:<22} ${value:>11,.2f}")

report = "\n".join(lines)
with open("evidence_pack.txt", "w", encoding="utf-8") as f:
    f.write(report + "\n")
```

**Two files, two readers:** a CSV a machine can use, and a page a person can read in ninety seconds. **Producing both is the job.**

**Say what you removed.** *"1,440 lines received; 1,387 after cleaning (6 unreadable dates dropped, 48 memo lines removed)."* A total with its provenance attached is **evidence**; a total on its own is an assertion.

**f-string formats worth memorising:**

| Format | `1234.5` becomes |
|---|---|
| `{v:.2f}` | `1234.50` |
| `{v:,.2f}` | `1,234.50` |
| `{v:>12,.2f}` | `    1,234.50` (right-aligned, width 12) |
| `{name:<22}` | left-aligned text, width 22 |

---

## Errors you will actually meet

| Error | Cause | Fix |
|---|---|---|
| `AttributeError: Can only use .str accessor with string values` | `.str` on a numeric column | `.astype(str)` first |
| `.sum()` returns glued-together text | the column is text, not numbers | the four-move chain |
| `RuntimeWarning: divide by zero encountered in log` | logging a column with zeros | filter to `> 0` first |
| `min` or `mean` is `-inf` | you already logged a zero | same fix |
| `ValueError: The truth value of a Series is ambiguous` | `and` where you need `&` | `&`, and bracket every condition |
| Row count grew after a merge | non-unique key on the right | check the key with `.duplicated()` |
| New `NaN`s after a merge | keys did not match | check `isna().sum()`, look for whitespace |
| A feature is the same in every row | measured against itself | use an outside reference; check `.nunique()` |

---

## The three processes

| Process | What it is | Where |
|---|---|---|
| **Data preparation** | cleaning, loading, merging into usable shape | Cluster C |
| **EDA** | analysing and summarising to see what matters | all of Lab01, Cluster D here |
| **Benchmark** | a baseline to measure improvements against | **Module 2** |

> 📌 **"Better features mean better results."** Better features also mean **simpler models** — a good feature has already done the hard thinking.
>
> **Feature engineering never adds information.** It makes information *usable*.

---

*Apeiron AI Training Academy · M1-W3-Lab02 · "Boundless Possibilities, Infinite Potential"*
