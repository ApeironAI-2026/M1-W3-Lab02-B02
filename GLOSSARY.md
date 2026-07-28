# 📖 Lab02 Glossary — Week 3, Session 2

**The Cozy Bean · M1-W3-Lab02 · Apeiron AI Training Academy**

*Every new word this week, one friendly line each. Alphabetical.*

---

### aggregation
Collapsing many rows into one summary number — a sum, a mean, a count. `groupby` makes the piles; the aggregation is what you work out for each pile.

### aggregation feature
A feature built by aggregating: *total paid to this supplier*, *number of transactions*, *average payment*. One row per group, one column per question.

### `as_index=False`
Keeps the grouping column as a **normal column** after a `groupby`, instead of moving it into the index. One less thing to think about when you merge later.

### `.astype(int)`
Turns `True`/`False` into `1`/`0`. Used after `get_dummies` because class describes one-hot output as "binary (0/1) features", and 0s and 1s are easier to read in a wide table.

### `.astype(str)`
Forces a whole column to text. **The first beat of the cleaning chain**, because `.str` operations only work on text columns.

### benchmark
A baseline standard you agree **before** you start improving things, so you can tell whether you improved anything. The third of the three processes. *(Module 2.)*

### coerce (`errors='coerce'`)
*"If you cannot read this value, do not crash — write `NaN` (or `NaT`) instead and carry on."* It fails **silently**, which is exactly why you always follow it with an `isna().sum()`.

### data leakage
Letting information from your test data influence how you prepare your training data — for example, scaling with the whole dataset's mean before splitting. A real and famous mistake; worth knowing the phrase.

### data preparation
Getting raw data into usable shape — cleaning, loading, merging. The first of the three processes, and most of this lab.

### encoding
Converting categorical data into numbers a model can work with. See **one-hot encoding**.

### feature
**A column that holds one useful fact.** Rows are observations (things that happened); columns are features (facts about them).

### feature engineering
Building features from raw data so a model — or a loan officer — can use them.

> **Turning a shoebox of receipts into the tidy one-page summary a loan officer can actually read.**
>
> It **never adds information.** It makes information *usable*.

### `.fillna({...})`
Fills missing values, taking a dictionary so each column gets its own fill: `df.fillna({'debit': 0.0, 'credit': 0.0})`.

### flag (rather than delete)
Marking an outlier with a boolean column and a reason, instead of removing the row. What you do when the outlier is real and explainable — like a loan tranche.

### `get_dummies`
The pandas function that one-hot encodes a column. `pd.get_dummies(df['channel'], prefix='channel')`.

### `.idxmax()`
Gives the **label** with the biggest value — the winner's *name*, not the number of times it won. `value_counts().idxmax()` is "the commonest value".

### imputation
The proper word for filling in missing values. **Numeric → mean or median; categorical → mode or a `"Missing"` label.** The goal is to keep your data size without inventing signal.

> **Fill from meaning, not from habit.** And remember every imputed value afterwards looks exactly like data — nothing marks it.

### key
The column two tables share, used to match their rows during a **merge**. Here: `counterparty_id`.

### `log1p`
`np.log1p(x)` computes `log(1 + x)`, so a zero gives `0.0` instead of `-inf` — no filter needed. But it treats "no payment" and "a \$0 payment" as the same thing. *(🚀 bonus.)*

### log transform
Replacing values with their logarithms, which **compresses large values far more than small ones**. Turns an unreadable skewed chart into a readable one. Nothing is deleted and no order changes.

> **You cannot take the log of zero.** Filter to positive values first, or `-inf` poisons your mean and your chart.

### merge
Stapling two tables together side by side, matching rows on a shared **key**. `pd.merge(left, right, on='key', how='left')`.

### `how='left'`
**Keep every row from the left table**, bringing over matches from the right; where the right has no match, you get `NaN`. Compare `how='inner'`, which keeps only rows present in **both** — and can silently make rows vanish.

### min-max scaling
See **normalisation**.

### mode
The **commonest** value in a column. What you fill a missing categorical value with. `df['c'].mode()[0]`.

### `-inf` (negative infinity)
What `np.log(0)` produces. **Not a small number — a broken one**, and it spreads: it poisons any mean, min or chart it touches.

### `NaT` (Not a Time)
The date version of `NaN`. What `to_datetime(errors='coerce')` writes when a date is unreadable.

### named aggregation
The readable way to build features:

```python
.agg(total_debit=('debit', 'sum'))
#     ^new column   ^old col  ^what to do
```

Gives flat, properly-named columns — no two-level headers to flatten.

### normalisation (min-max scaling)
Rescaling a column into a fixed range, usually 0…1: `(x − min) / (max − min)`. The smallest value becomes exactly 0, the largest exactly 1.

### `.nunique()`
How many **different** values. `('date', 'nunique')` as an aggregation counts *active days* — five transactions on one day is one day.

### observation
One row — one thing that happened. Also called an *instance*.

### one-hot encoding
Turning one text column into **several 0/1 columns, one per value, with exactly one `1` per row**. That single "hot" value is where the name comes from.

> **The cost is columns.** Four values give four columns; a column with 500 names gives 500. Encode the small categoricals; think hard about the big ones. **Never encode an identifier.**

### outlier
A value far enough from the rest to be worth questioning.

> **An outlier is a question, not a verdict.** Sometimes the answer is "a typo". Sometimes it is *"the loan the bank just gave you"* — and then you flag it, explain it, and **keep** it.

### `pd.concat([a, b], axis=1)`
Sticks tables together **side by side** (`axis=1`) or **stacked** (`axis=0`, the default). Used to attach one-hot columns back onto the table.

### `pd.to_numeric`
The final beat of the cleaning chain: turns text into numbers, with `errors='coerce'` writing `NaN` for anything still unreadable.

### provenance
The record of where a number came from and what was removed to produce it. *"1,440 lines received; 1,387 after cleaning."* **A total with its provenance is evidence; a total on its own is an assertion.**

### recency feature
A feature measuring *how long since* something last happened. **Must be measured against a fixed date from outside the data** — today, the application date, the review date.

> Measure it against the group's own latest date and the answer is **always 0, for everybody.** A feature identical in every row carries no information.

### scaling
Putting columns with wildly different ranges onto a common ruler, so an algorithm does not treat a bigger number as a more important number. Two ways: **normalisation** and **standardisation**.

**Who cares:** K-means, linear regression, neural networks. *(Tree-based methods largely do not.)*

### skew
When one tail of a distribution stretches much further than the other, pulling the **mean away from the median**. **Money is always skewed.**

### standardisation (z-score scaling)
Rescaling a column to **mean 0, standard deviation 1**: `(x − mean) / std`.

> 🔙 **This is the same formula you used to find outliers in Lab01.** There it spotted a weird value; here it prepares a column for a model. **One formula, two jobs.**

### `str` dtype
What pandas 3 calls a text column. Your instructor's older pandas called it `object`. Same column, different label.

### `.str`
The doorway to text operations on a whole column — `.str.replace()`, `.str.len()`. **Only works on text columns**; `.astype(str)` first if you are not certain.

### `~` (tilde) — NOT
pandas' `not`, alongside `&` for and and `|` for or.

```python
df[~((df['credit'] == 0) & (df['debit'] == 0))]
```

**Bracket the whole condition** — `~` applied to only the first part means something completely different, and runs without complaint.

### Timedelta
What you get when you subtract two dates — a *duration*, like `6 days 00:00:00`. **`.dt.days`** turns it into the number 6.

### `\N`
A literal backslash-N that databases write to mean *"no value here"*. Arrives in a CSV as an ordinary word, so `read_csv` leaves it alone and you have to replace it yourself.

---

## The four-move cleaning chain

| Beat | Move | Why |
|---|---|---|
| **1** | `.astype(str)` | `.str` only works on text |
| **2** | `.str.replace(',', '', regex=False)` | a comma stops a number being a number |
| **3** | `.replace({'\N': np.nan, 'None': np.nan, '': np.nan})` | turn "nothing" markers into real gaps |
| **4** | `pd.to_numeric(errors='coerce')` | finally, be a number |

**Skip beat 2 and nothing crashes — your biggest values silently become `NaN`.**

---

## The three processes

| | What it is | Where |
|---|---|---|
| **Data preparation** | cleaning, loading, merging | Cluster C |
| **EDA** | analysing and summarising | Lab01, and Cluster D |
| **Benchmark** | a baseline to measure against | Module 2 |

> 📌 **"Better features mean better results."** Better features also mean **simpler models** — a good feature has already done the hard thinking.

---

*Apeiron AI Training Academy · M1-W3-Lab02 · "Boundless Possibilities, Infinite Potential"*
