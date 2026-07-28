# ☕ M1-W3-Lab02 — The Evidence Pack: Turning a Bank Statement into Features

### Feature Engineering
**Apeiron AI Training Academy** · *"Boundless Possibilities, Infinite Potential"*

| | |
|---|---|
| **Module** | M1: AI/ML Fundamentals |
| **Week** | Week 3 |
| **Lab** | Lab02 — The Evidence Pack |
| **Duration** | **≈ 1 hour** of lab work (**plus ~10 minutes of setup, not counted**) |
| **Difficulty** | ⭐⭐⭐ Beginner, level 3 — **you speak pandas now** |

> 🛋️ **Aim for one sitting of about an hour.** If you do need to pause, the natural break is after **Cluster C**, when the statement is finally clean. Everything before that break is repair work; everything after is building.

### What you learned in class (and will now make your own)

What a feature is · why feature engineering matters · the three processes (data preparation → EDA → benchmark) · **imputation** · **outlier treatment** · **log transform** · **one-hot encoding** · **scaling** (min-max and z-score) · `pd.to_datetime(errors='coerce')` · industrial-scale string cleaning · `~` as NOT · named aggregations · `pd.merge`

---

## 1. ☕ The Story

Mrs Adeyemi's email is four sentences long and one of them is a problem.

> *"Thank you for the trial-season analysis, which was genuinely well done. The first tranche has been released. Before I can sign off the full disbursement I need to see how the business **behaves**, not just what it **earned**. Please send whatever you have that shows the last eighteen months."*

**"How the business behaves."** Not totals. Totals you already sent — 244 bills, an average of \$19.79, a p-value of 0.71, and it was enough to get you this far. But a loan officer releasing the rest of the money wants something else: *does money arrive reliably? do you pay your suppliers? did the account ever go dry? and is the shop that earned the first tranche still the same shop?*

There is exactly one document that answers all of that, and you have been ignoring it for eighteen months because it is unbearable to look at.

**The bank statement.**

You request the full export. It arrives as a CSV with **1,440 rows** in it, and you open it, and:

```text
                      date   debit  credit closing_balance       counterparty
0  2025-05-01T00:00:00.000      \N  376.73        5,176.73    Card Settlement
1  2025-05-01T00:00:00.000      \N  187.40        5,364.13       Cash Deposit
2  2025-05-01T00:00:00.000  304.71     NaN        5,059.42   Beans Direct Ltd
```

**Every single column is text.** The money has **commas inside it**. Where a value should be absent there is a literal `\N`, or the word `None`, or nothing at all. Forty-eight rows record no money moving whatsoever. Six dates say `not recorded` or, magnificently, `31/02/2026`.

You cannot add up a single column of this file. `df['debit'].sum()` does not give you a total — it gives you every value **glued end to end** in one absurd string.

**This is the most realistic thing in the entire course.** This is what an export from a real financial system actually looks like, and learning to fix it is not a chore on the way to the interesting part. It *is* the interesting part, and it is most of what data work actually is.

### What feature engineering means, in one sentence

By the end of today you will have turned that mess into a tidy one-page table. That transformation has a grand name — **feature engineering** — and here is the honest version:

> ## Feature engineering is turning a shoebox of receipts into the tidy one-page summary a loan officer can actually read.

That is it. You take raw records — one row per thing that happened — and you build columns that *answer questions*. "Total paid to suppliers." "Days since money last came in." "Busiest day of the week." None of those exist in the statement. All of them are in your evidence pack by teatime.

It was put more formally in class, and it is worth keeping:

> 📌 **"Better features mean better results."**
>
> 📌 *"No algorithm alone, to my knowledge, can supplement the information gain given by correct feature engineering."*

Mrs Adeyemi is the algorithm this week. She eats the same tidy table a model would.

Every idea in this lab is a physical thing on your kitchen table:

- a **feature** is a column that answers a question
- **cleaning** is unfolding crumpled receipts before you can read them
- **imputation** is deciding what to write in the box the till smudged
- an **outlier** is the one enormous credit — *and you know exactly what it is*
- the **log transform** is stepping back so the giant stops blocking the view
- **encoding** is translating "transfer" into something a machine can add up
- **`merge`** is stapling two summary pages together
- and the **evidence pack** is what goes in the envelope

### Why this matters in real life (and in AI/ML)

- **This is the job.** Surveys of working data scientists put data preparation at 60–80% of the work. Not modelling. This.
- **Models eat features, not files.** Every model in Module 2 will be handed a table exactly like the one you build today. The quality of that table sets the ceiling on everything the model can do.
- **`\N` is real.** So are commas in numbers, and `None` as a word, and six broken dates in 1,440 rows. Every export from every real system has its own version of this, and the four moves you learn in STEP 5 handle most of them.
- **And the judgement calls are yours.** Fill or drop? Flag or delete? Log or leave? A library can do the arithmetic. Nothing can make those decisions for you — which is precisely why this job is not going away.

### ✅ Success Criteria — what you will be able to produce

- `python scripts/02_meet_the_statement.py` — the horror, honestly documented
- `python scripts/04_string_surgery.py` — **text turned back into money**
- `python scripts/05_fill_and_filter.py` — 1,440 rows down to the 1,392 that mean something
- **four charts** in `charts/`, including the balance chart with your whole spring in it
- `python scripts/08_outlier_or_loan.py` — the IQR fence, and a judgement no formula could make
- `python scripts/10_one_hot_channel.py` and `11_scaling_by_hand.py` — the two techniques from class
- `python scripts/15_evidence_pack.py` — **`engineered_counterparties.csv` + `evidence_pack.txt`**
- …and eight practice problems, including a capstone that answers a question I never asked you.

---

## 2. 🎯 Learning Objectives

By the end of this lab you will be able to:

1. Define a **feature**, and explain rows-as-observations and columns-as-features.
2. Say why feature engineering matters, in the three terms used in class.
3. Name the three processes: **data preparation → EDA → benchmark**.
4. Convert a text date column with `pd.to_datetime(errors='coerce')` and explain what `coerce` does.
5. Turn a column of text that looks like money into **actual money**, in four deliberate moves.
6. Choose a fill value because of what the gap **means**, not because a rule said so.
7. Use **`~`** as NOT, and say what it does to a boolean condition.
8. State the **imputation** rules for numeric and categorical columns.
9. Apply the IQR fence to your own data and **decide whether to flag or delete**.
10. Apply a **log transform** safely, and explain why zeros must be excluded first.
11. **One-hot encode** a categorical column and read a row of it aloud.
12. **Scale** a column two ways — min-max and z-score — with plain arithmetic.
13. Build aggregation features with **named aggregations**, one at a time.
14. Join two summary tables with **`pd.merge(..., how='left')`**.
15. Assemble and ship an **evidence pack**: a feature CSV and a one-page note.

---

## 3. 🔧 Before You Start

> ### ⏱️ About 10 minutes. **Nothing new to install this week.**

### 3.1 If you did Lab01 today

You are already set up. Open your **`Lab02`** folder (**File → Open Folder…**), open a terminal, and run:

```text
py scripts/00_check_setup.py
```

Six ticks and you are away.

### 3.2 If you are starting fresh

```text
py -m pip install pandas matplotlib seaborn scipy google-play-scraper
py scripts/00_check_setup.py
```

📺 **Expected output:**

```text
=== THE COZY BEAN -- KITCHEN INSPECTION (WEEK 3) ===

  ✅  pandas               3.0.3
  ✅  numpy                2.4.6
  ✅  matplotlib           3.10.9
  ✅  seaborn              0.13.2
  ✅  scipy                1.17.1
  ✅  google_play_scraper  1.2.7

All six ready. You can start the lab.
```

*(This lab never scrapes anything — `google_play_scraper` is checked only so the two labs share one setup script. If it is the single thing missing, you can start anyway.)*

### 3.3 Where the data lives

| File | What it holds |
|---|---|
| `data/cozybean_statement.csv` | **The Cozy Bean's bank statement — 1,440 rows × 8 columns**, 2025-05-01 to 2026-10-31 |

**This lab needs no internet at all.** Not one line of it.

The eight columns:

| Column | What it is |
|---|---|
| `date` | when it happened — **as text**, and six of them are broken |
| `debit` | money **out** — as text, with commas |
| `credit` | money **in** — as text, with commas |
| `reference` | the bank's own reference for the transaction |
| `closing_balance` | the running balance after that line — as text, with commas |
| `counterparty_id` | a short code: `c1`, `c2`, … — **the key we group and merge on** |
| `counterparty` | who the money went to or came from |
| `channel` | how it moved: `card`, `cash`, `transfer`, `standing_order` |

### 3.4 "If you see this, do this"

| What you see | What to do |
|---|---|
| `FileNotFoundError: … 'data/cozybean_statement.csv'` | 🔙 Wrong folder. `pwd` must end in `Lab02`. |
| `AttributeError: Can only use .str accessor with string values` | You skipped `.astype(str)`. STEP 5 explains exactly why it comes first. |
| `RuntimeWarning: divide by zero encountered in log` | You logged a column containing zeros. STEP 11 is entirely about this. |
| **The terminal froze after a chart appeared** | It is waiting for you to close the chart window — possibly hiding behind VS Code. The PNG is already saved. |
| `ValueError: The truth value of a Series is ambiguous` | 🔙 Week 2 — you used `and` where you need `&`. Bracket every condition. |

### 3.5 📌 A note about your screen versus your instructor's

Two harmless differences, same as Lab01:

- **Text columns** show as `str` on your screen, `object` on your instructor's.
- **Dates** show as `datetime64[us]`, theirs `datetime64[ns]`.

And one difference that is **not** cosmetic, which this lab is honest about at STEP 5: **your instructor's copy of this data happened to arrive with the money columns already numeric.** Yours has not. That means the cleaning chain — which ran defensively in class and visibly changed nothing — does real, visible work here. You get the better version of that lesson.

---

## 4. 📖 Guided Walkthrough

Eighteen steps in nine clusters.

> ### 📌 One thing to notice as you go
>
> From STEP 8 onwards, **every script begins by repeating the same nine-line cleaning block.** That is deliberate: it means any script runs on its own, in any order, without depending on what you ran an hour ago.
>
> It will also start to annoy you. **Good.** Practice problem **p07** is where that annoyance becomes a function — and noticing "I have typed this too many times" is a genuine professional instinct, not a complaint.

---

## ☕ Cluster A — What a Feature Actually Is

*Script for this cluster:* **`scripts/01_what_is_a_feature.py`**

---

### STEP 1 — Rows are observations, columns are features

▶ *In your script:* Section 1 of `scripts/01_what_is_a_feature.py`

🎯 **Objective:** Learn the vocabulary, on a table small enough to see all of.

☕ **Story moment:** Before the statement — which is horrible — here are three days of the shop, typed out by hand. Four facts about each day.

🧠 **The idea in plain English:** It was said precisely in class: input data is *"tabular, consisting of rows (instances or observations) and columns (variables or attributes), and these attributes are often known as **features**."*

Translated:

| Word | Means | Here |
|---|---|---|
| **observation** (or instance, or row) | one thing that happened | one day the shop was open |
| **feature** (or variable, or attribute, or column) | one fact about that thing | how many cups you sold |

That is the whole vocabulary. **A feature is a column that tells you something useful.** Nothing more mysterious than that.

Two examples from other fields were given in class, and they are worth ten seconds because they show how far the idea stretches: in **computer vision** an image is the observation and *a line within it* could be the feature; in **NLP** a document is the observation and *the word count* could be the feature. Same idea, wildly different data.

💻 **The code:**

```python
days = pd.DataFrame({
    "date":         ["2026-10-29", "2026-10-30", "2026-10-31"],
    "cups_sold":    [138, 152, 161],
    "muffins_sold": [29, 33, 35],
    "takings":      [529.25, 571.40, 604.75],
})
print(days)
```

📺 **Expected output:**

```text
=== STEP 1: ROWS AND COLUMNS HAVE PROPER NAMES ===
         date  cups_sold  muffins_sold  takings
0  2026-10-29        138            29   529.25
1  2026-10-30        152            33   571.40
2  2026-10-31        161            35   604.75

Each ROW is one OBSERVATION -- one day the shop was open.
Each COLUMN is one FEATURE -- one fact about that day.

Observations (rows):  3
Features (columns):   4

That is the whole vocabulary. A feature is a column that
tells you something useful. Nothing more mysterious.
```

✅ **Verify:** Three rows, four columns.

🎤 **Try it yourself (30 seconds):** In the flights table from Lab01, what was the observation and what were the features? *(One flight; nineteen facts about it.)* Same two words, a third of a million rows.

---

### STEP 2 — The features you make yourself

▶ *In your script:* Section 2 of `scripts/01_what_is_a_feature.py`

🎯 **Objective:** Build your first feature, and understand why anyone bothers.

☕ **Story moment:** Nobody recorded "takings per cup". But it is obviously useful — it is roughly *"what is the average customer worth?"* — and you have everything you need to build it.

🧠 **The idea in plain English:** **Feature engineering** is the pre-processing step that *extracts features from raw data*. It does not mean inventing information. It means **rearranging information you already have into a shape that answers a question.**

`takings / cups_sold` is not new data. It is two columns you had, combined into a fact neither could state alone.

💻 **The code:**

```python
days["per_cup"] = (days["takings"] / days["cups_sold"]).round(3)
```

📺 **Expected output:**

```text
=== STEP 2: THE FEATURES YOU MAKE YOURSELF ===
Nobody recorded 'takings per cup'. But we can build it:

         date  cups_sold  takings  per_cup
0  2026-10-29        138   529.25    3.835
1  2026-10-30        152   571.40    3.759
2  2026-10-31        161   604.75    3.756

That new column is FEATURE ENGINEERING, and you just did it.
Two columns you had -> one column you did not have, that
answers a question neither of them could answer alone.

It was put like this in class, and it is worth remembering:

    "Better features mean better results."

Better features also mean SIMPLER models -- because a good
feature has already done the hard thinking.
```

**About \$3.80 a cup**, holding steady across three days. 🔙 And notice it sits nicely between your menu prices — a latte is \$3.50, a cappuccino \$4.00 — which is a sanity check that the feature means what you think it means.

**Why anyone bothers.** Three reasons were given in class and they are all true:

- **Better features mean better results.** *"The quality of data and features you provide directly determines the output."*
- **Better features mean simpler models.** A good feature has already done the thinking, so the model has less to work out.
- **Better features mean flexibility.** *"Sometimes even with the wrong model, better features produce great predictions."*

**The three processes**, which is the shape of this whole week:

| Process | What it is | Where you did it |
|---|---|---|
| **Data preparation** | getting raw data into usable shape — cleaning, loading, merging | **Cluster C today** |
| **Exploratory analysis (EDA)** | analysing and summarising to see what matters | **all of Lab01**, and Cluster D today |
| **Benchmark** | a baseline standard to measure improvements against | **Module 2** — awareness only today |

**Benchmark** is the one you have not done. It means: agree a target and a baseline *before* you start improving things, so you can tell whether you improved anything. Today's equivalent is Mrs Adeyemi's judgement, and today's baseline is the totals you already sent her.

⚠️ **Common mistake:** Believing feature engineering creates information. It cannot. `per_cup` contains nothing that was not already in `takings` and `cups_sold` — it just puts it where a human can see it. **A feature makes information usable; it never adds any.**

✅ **Verify:** A `per_cup` column reading 3.835, 3.758, 3.756.

🎤 **Try it yourself (60 seconds):** Build one more: `muffins_per_cup`. Do more customers buy a muffin on busier days? *(Three rows is not enough to answer that — but you have now built two features and the second one took you fifteen seconds.)*

---

## ☕ Cluster B — Meet the Statement

*Scripts for this cluster:* **`scripts/02_meet_the_statement.py`**, **`scripts/03_eda_pass.py`**

---

### STEP 3 — Eighteen months of horror

▶ *In your script:* the whole of `scripts/02_meet_the_statement.py`

🎯 **Objective:** Profile the statement, and catalogue exactly what is wrong with it.

☕ **Story moment:** 🔙 Lab01 STEP 1: *"before you trust a number, interrogate the table it came from."* Let us interrogate this one. It will not go well, and that is the point.

🧠 **The idea in plain English:** Same opening moves as every table you will ever meet: `shape`, `head()`, `info()`. What is different is what they tell you.

💻 **The code:**

```python
df = pd.read_csv("data/cozybean_statement.csv")
print("Shape (rows, columns):", df.shape)
print(df[['date', 'debit', 'credit', 'closing_balance', 'counterparty']].head())
df.info()
print(df['debit'].head(12).to_list())
```

📺 **Expected output:**

```text
=== STEP 3: 18 MONTHS OF THE COZY BEAN'S BANK ACCOUNT ===
Shape (rows, columns): (1440, 8)

The first five lines:
                      date   debit  credit closing_balance       counterparty
0  2025-05-01T00:00:00.000      \N  376.73        5,176.73    Card Settlement
1  2025-05-01T00:00:00.000      \N  187.40        5,364.13       Cash Deposit
2  2025-05-01T00:00:00.000  304.71     NaN        5,059.42   Beans Direct Ltd
3  2025-05-01T00:00:00.000   66.31     NaN        4,993.11           Dairy Co
4  2025-05-01T00:00:00.000  110.16     NaN        4,882.95  Muffin Top Bakery

=== THE INVENTORY ===
<class 'pandas.DataFrame'>
RangeIndex: 1440 entries, 0 to 1439
Data columns (total 8 columns):
 #   Column           Non-Null Count  Dtype
---  ------           --------------  -----
 0   date             1440 non-null   str  
 1   debit            1128 non-null   str  
 2   credit           1043 non-null   str  
 3   reference        1440 non-null   str  
 4   closing_balance  1440 non-null   str  
 5   counterparty_id  1440 non-null   str  
 6   counterparty     1440 non-null   str  
 7   channel          1440 non-null   str  
dtypes: str(8)
memory usage: 198.0 KB

=== NOW LOOK AGAIN, AND BE HORRIFIED ===
Every single column says 'str'. Every one. Including the money.

Some actual cells from the debit column:
['\\N', '\\N', '304.71', '66.31', '110.16', '1,850.00', '100.04', nan, '\\N', '0.00', '\\N', '162.72']

Read that list slowly. FIVE different things are wrong:
  '304.71'    a number... stored as text
  '1,850.00'  a number with a COMMA in it
  '0.00'      a real zero, which we will have to think about
  '\\N'        a database's way of writing 'nothing here'
  'None'      a Python word that leaked into the file

And one thing that is already half-fixed: that bare 'nan' in
the list. Some cells in the file are genuinely empty, and
read_csv is kind enough to turn those into NaN for us on the
way in. The other three flavours of 'nothing' it left alone,
because as far as it can tell they are ordinary words.

And the dates are text too:
['2025-05-01T00:00:00.000', '2025-05-01T00:00:00.000', '2025-05-01T00:00:00.000']

What we have got, in one sentence: 1,440 rows of evidence
for a loan application, and not one usable number in sight.
STEPs 4 to 9 fix that. Then the real work starts.
```

**Look at the `Dtype` column of that inventory: `str`, eight times.** `dtypes: str(8)`. There is not one numeric column in a **bank statement**.

**And read that list of twelve actual cells**, because it is the whole of Cluster C's to-do list:

| What you see | The problem |
|---|---|
| `'304.71'` | a number in a text costume |
| `'1,850.00'` | **a comma inside a number** — this one is the killer |
| `'0.00'` | a real zero, which is genuinely different from "nothing" |
| `'\N'` | a database's marker for "no value here" |
| `'None'` | the Python word, leaked into a text file as a *word* |
| `nan` | genuinely empty — and `read_csv` already handled this one |

**That last row is worth pausing on.** `read_csv` spotted the truly blank cells and turned them into `NaN` on the way in, all by itself. The other three flavours of nothing it left alone — because `\N` and `None` are, as far as a CSV reader can tell, ordinary words. **You get some help for free, and then you are on your own.**

**Notice too what `info()` can already tell you**: `debit` has 1,128 non-null and `credit` has 1,043. Neither is 1,440, and 1,128 + 1,043 = 2,171, which is more than 1,440. So some rows have a value in *both* columns — those will be the `0.00` ones — and some have neither.

⚠️ **Common mistake:** Trusting `head()` alone. The first five rows look almost respectable — you can *read* `304.71`. It is only `info()` that tells you pandas thinks it is a word.

✅ **Verify:** `(1440, 8)` and `dtypes: str(8)`.

🎤 **Try it yourself (60 seconds):** Run `df['credit'].head(12).to_list()`. Same five problems, different column. Then try `df['debit'].max()`. You get `'\N'` — because the "largest" *word*, alphabetically, is the one starting with a backslash. **It answered your question. It just answered a different question than the one you meant.**

---

### STEP 4 — Make the dates real, and find the broken ones

▶ *In your script:* the whole of `scripts/03_eda_pass.py`

🎯 **Objective:** Convert a text date column forgivingly, and deal with what fails.

☕ **Story moment:** Before any money, the dates — because "the last eighteen months" is a claim you cannot make until the dates are real.

🧠 **The idea in plain English:** 🔙 Lab01 STEP 16 used `pd.to_datetime()`. Here it gets one extra argument that matters enormously:

```python
df['date'] = pd.to_datetime(df['date'], errors='coerce')
```

**What `errors='coerce'` means, in one sentence: *if you cannot read a date, do not crash — write `NaT` instead and carry on.***

`NaT` is "Not a Time" — 🔙 the date version of `NaN`. Without `coerce`, one unreadable date anywhere in 1,440 rows kills the whole script. With it, the failures become *countable*, which is far more useful than a traceback.

💻 **The code:**

```python
df['date'] = pd.to_datetime(df['date'], errors='coerce')
bad = df['date'].isna().sum()
print(f"Dates the bank's system mangled: {bad}")

df = df.dropna(subset=['date'])

print("First transaction:", df['date'].min().date())
print("Last transaction: ", df['date'].max().date())
print(df['date'].value_counts().sort_index().head())
```

📺 **Expected output:**

```text
=== STEP 4: MAKE THE DATES REAL ===
Before: str
After:  datetime64[us]

errors='coerce' means: if you cannot read a date, do not
crash -- write NaT instead ('Not a Time') and carry on.

Dates the bank's system mangled: 6

Here they are, straight from the file:
             date               reference      counterparty
189  not recorded  1054800004388-20250712   Card Settlement
248    31/02/2026            TT25217VFWYN  Beans Direct Ltd
326  not recorded  1054800004388-20250902   Card Settlement
616    31/02/2026            TT253565RCV0    Statement Memo
761  not recorded            TT260455Q0MF      Cash Deposit
889    31/02/2026  1054800004388-20260404   Card Settlement

'not recorded' is not a date. '31/02/2026' is not a date
either -- February does not have 31 days.

Rows before: 1440   after dropping the 6: 1434
Six rows out of 1,440 is 0.4%. Dropping them is honest and
cheap. Keeping them would poison every date calculation.

=== THE PERIOD WE ARE SHOWING THE BANK ===
First transaction: 2025-05-01
Last transaction:  2026-10-31
Days covered:      548

Busiest five days by number of transactions:
date
2025-05-01    7
2026-09-01    7
2025-06-06    6
2025-06-28    6
2025-10-25    6
Name: count, dtype: int64

Transactions per day, earliest first (first five days):
date
2025-05-01    7
2025-05-02    1
2025-05-03    2
2025-05-04    2
2025-05-05    5
Name: count, dtype: int64
```

**Six broken dates, and look at how they are broken** — two different ways:

- **`not recorded`** — somebody's system wrote a *sentence* into a date column.
- **`31/02/2026`** — this one is sneakier. It *looks* like a date. It has the right shape. But **February does not have 31 days**, so it is not a date at all, it is a typo with good posture.

`errors='coerce'` caught both without knowing anything about calendars.

**Then the decision: drop them.** Six rows out of 1,440 is **0.4%**. There is no honest way to guess when they happened, and keeping them would mean every date calculation in this lab has to special-case them. 🔙 Week 2's rule applies: **drop when the row is too damaged to trust.** A transaction with no date is exactly that.

**And now you can answer Mrs Adeyemi's question:** 2025-05-01 to 2026-10-31, **548 days**. Eighteen months, as requested.

**One last detail worth catching.** Look at the busiest days: the 1st of the month appears twice in the top five. Rent, wages and standing orders all land on the same dates, so month-boundaries are busy. **That is a real rhythm in your business, and it will show up again in STEP 16.**

⚠️ **Common mistake:** Using `errors='coerce'` and then never checking what it coerced. `coerce` fails *silently* — that is the whole point of it — so **if you do not count the `NaT`s, you will never know how much of your data quietly evaporated.** Always follow a coerce with an `isna().sum()`.

✅ **Verify:** `Dates the bank's system mangled: 6`, then 1440 → 1434, and 548 days.

🎤 **Try it yourself (60 seconds):** Remove `errors='coerce'` and rerun. You get a `ValueError` and the script dies on row 189 — no date range, no analysis, nothing. **Now you know exactly what that argument is buying you.**

> 📌 **You saw this in class:**
>
> ```python
> df['date'] = pd.to_datetime(df['date'], errors='coerce')
>
> missing_data = df.isnull().sum()
> print(f"Missing Data:\n{missing_data}")
> print(df.describe())
> ```
>
> and
>
> ```python
> date_range = df['date'].min(), df['date'].max()
> transaction_counts = df['date'].value_counts().sort_index()
> ```
>
> Same calls. Your instructor's copy had no broken dates to catch, so `coerce` sat there quietly doing nothing visible. **Yours has six**, so you get to watch it work.

---

### 🧠 Quick Quiz #1 — answer from memory, before peeking

*(Answers are in the **Answer Key** at the end. No scrolling ahead.)*

**Q1.** What is a "feature", in one line?

- A) A row of a table, describing one observed thing
- B) A column of a table, holding one useful fact
- C) A machine-learning model's prediction output
- D) A missing value that has been filled in

**Q2.** What does `errors='coerce'` do in `pd.to_datetime()`?

- A) It converts every date into a single consistent format
- B) It raises an error naming the first unreadable date
- C) It writes `NaT` where a date cannot be read, without crashing
- D) It removes rows with unreadable dates automatically

**Q3.** `df.info()` says every column is `str`, including the money. What follows?

- A) Nothing can be added up until those columns are converted
- B) The file is corrupted and must be requested again
- C) The money columns contain no usable values at all
- D) pandas will convert them automatically when you use `.sum()`

---

## ☕ Cluster C — Cleaning: The Best Twenty Lines of the Week

*Scripts for this cluster:* **`scripts/04_string_surgery.py`**, **`scripts/05_fill_and_filter.py`**

---

### STEP 5 — Numbers wearing string costumes

▶ *In your script:* the whole of `scripts/04_string_surgery.py`

🎯 **Objective:** Turn a column of text that *looks* like money into money you can actually add up.

☕ **Story moment:** You have the statement open. The `debit` column shows `304.71`, `66.31`, `1,850.00`. Those are numbers. Obviously they are numbers. So you ask for the total:

```python
print(df['debit'].sum())
```

and the bank's computer hands you `\N\N304.7166.31110.16` — every value **glued end to end**.

Nothing is broken. pandas did exactly what you asked. You asked it to add up some **text**, and the way you add text is to stick it together — 🔙 Week 1, `"cozy" + "bean"`.

🧠 **The idea in plain English:**

The bank's export system wrote your money out as **words, not numbers**. Four things are wrong with it, and each needs its own move:

| What is wrong | Example cell | The move |
|---|---|---|
| Thousands separators | `1,850.00` | strip the commas |
| A database's "nothing here" marker | `\N` | turn it into a real gap |
| A Python word that leaked into the file | `None` | turn it into a real gap |
| A genuinely empty cell | | turn it into a real gap |

Only then can you say "now please be a number".

> 🔙 **Remember from Week 1:** `int("42")` turns text into a number. `int("42 ")` with a stray space still works — but `int("4,2")` does not. **This is that same casting lesson, at industrial scale.** One value versus fourteen hundred; the idea has not changed at all.

💻 **The code — one move at a time:**

```python
# Beat 1 -- make absolutely sure every cell is text before we do text things to it
df['debit'] = df['debit'].astype(str)

# Beat 2 -- strip the thousands separators
df['debit'] = df['debit'].str.replace(',', '', regex=False)

# Beat 3 -- turn all three flavours of "nothing" into a real, countable gap
df['debit'] = df['debit'].replace({'\\N': np.nan, 'None': np.nan, '': np.nan})

# Beat 4 -- NOW ask it to be a number
df['debit'] = pd.to_numeric(df['debit'], errors='coerce')
```

**Each beat, in one line:**

- **Beat 1 — `.astype(str)`.** Force the whole column to text. It is *already* text, so this looks pointless — but it guarantees the next three moves are safe. See the ⚠️ below for what happens without it.
- **Beat 2 — `.str.replace(',', '', regex=False)`.** `.str` is the door to text operations on a whole column. `regex=False` says "treat that comma as a literal comma", which is both faster and clearer.
- **Beat 3 — `.replace({...})`.** Note: **no `.str`** here. This one swaps whole cell *values*, not pieces of text within them, and it takes 🔙 a Week-1 dictionary: `{find: replace}`.
- **Beat 4 — `pd.to_numeric(..., errors='coerce')`.** 🔙 Same `coerce` as STEP 4: anything still unreadable becomes `NaN` instead of crashing.

📺 **Expected output:**

```text
=== BEFORE: what the bank actually sent us ===
0        \N
1        \N
2    304.71
3     66.31
4    110.16
Name: debit, dtype: str

Ask for the total and pandas does exactly what you said:
  .sum() on that -> \N\N304.7166.31110.16
  ...glued end to end, not added up. Because it is TEXT,
  and the way you add text is to stick it together.

=== AFTER: four small moves later ===
0       NaN
1       NaN
2    304.71
3     66.31
4    110.16
Name: debit, dtype: float64

  .sum() on that -> 481.18

Look at the dtype on those two blocks. It went from 'str'
to 'float64'. That one word changing is the whole STEP.

Real gaps we can now count: 565
Nothing was invented. '\\N', 'None' and '' became NaN --
we recorded an absence instead of guessing a value.

=== ALL THREE MONEY COLUMNS, DONE ===
debit              float64
credit             float64
closing_balance    float64
dtype: object

Gaps in each:
debit              565
credit             727
closing_balance      0
dtype: int64

closing_balance has NO gaps -- the bank always printed a
running balance. It only ever needed its commas removed.
```

**Look at `dtype` on the two blocks. `str` → `float64`. That one word changing is the whole STEP.**

And `.sum()` went from `\N\N304.7166.31110.16` to **`481.18`**. From nonsense to an actual total, in four lines.

**Look at rows 0 and 1.** `\N` did not vanish — it became **`NaN`**. 🔙 Week 2's "there was nothing here". That is the honest outcome: **we did not invent a value, we recorded an absence.** STEP 6 decides what to do about it.

**And notice the third column.** `closing_balance` has **zero** gaps — the bank printed a running balance on every single line. Beats 3 and 4 ran on it and had nothing to do. **That is what defensive code looks like**, and it is why you write all four beats even when you only need two.

**The final `for` loop is worth a look too.** Rather than typing the same four beats three times, the script loops over the remaining two columns — 🔙 a Week-1 `for` loop, saving you eight lines.

⚠️ **Common mistake — and this is the one:** skipping Beat 1. The sneakiest version is running the chain a **second** time: after Beat 4 the column *is* numbers, so Beat 2 without Beat 1 now hits a numeric column — and `.str` on numbers gives you:

```text
Traceback (most recent call last):
  File "your_file.py", line 13, in <module>
    print(df['debit'].str.replace(',', '', regex=False).head())
          ^^^^^^^^^^^^^^^
AttributeError: Can only use .str accessor with string values, not floating. Did you mean: 'std'?
```

**Translated:** *"`.str` is for text columns and this one now holds floating-point numbers."* `.astype(str)` costs nothing and makes the other three moves safe **every** time you run them. *(Python's helpful "Did you mean: 'std'?" is a red herring — you did not want `std`, you wanted `.astype(str)` first.)*

✅ **Verify:** `dtype: float64` in the AFTER block, `.sum()` printing `481.18`, gaps of 565 / 727 / 0.

🎤 **Try it yourself (60 seconds):** Comment out **Beat 2 only** — the comma-stripping line — and rerun. The commas survive, `pd.to_numeric` cannot read `1,850.00`, and `errors='coerce'` quietly turns **your biggest payments** into `NaN`. Count the gaps now: far more than 565.

**That is the most dangerous bug in this entire lab.** It does not crash. It does not warn you. It silently deletes your largest numbers — and every total you compute afterwards is too small, and nothing on your screen says so.

> 📌 **You saw this in class:** your instructor ran this chain as one expression —
>
> ```python
> df['credit'] = (
>     df['credit']
>     .astype(str)
>     .str.replace(',', '', regex=False)
>     .replace({'\\N': np.nan, 'None': np.nan, '': np.nan})
> )
> df['credit'] = pd.to_numeric(df['credit'], errors='coerce')
> ```
>
> and the same again for `debit` and `closing_balance`. **Identical moves** — we have simply put each on its own line so you can watch them land one at a time.
>
> **And one honest note.** In the class's own recorded run, `df.info()` showed `debit` and `credit` had *already* loaded as `float64` — that particular export happened to arrive clean, so this chain ran **defensively** and changed nothing anybody could see. **Your statement is not so lucky**, which is why you can watch every move do real work. Do not conclude from the class notebook that money columns usually arrive as text; conclude that a careful analyst writes this chain either way.

---

### STEP 6 — What a gap *means*, and the `~` operator

▶ *In your script:* Sections 1–2 of `scripts/05_fill_and_filter.py`

🎯 **Objective:** Choose a fill value from meaning rather than habit, and meet `~`.

☕ **Story moment:** You have 565 gaps in `debit` and 727 in `credit`. 🔙 Lab01 said *"on skewed data, fill with the median"*. Money is skewed. So: median?

**No. And understanding why not is worth more than the rule.**

🧠 **The idea in plain English:** **Think about what the gap means.**

Every line of a bank statement is money **in** *or* money **out** — never both. A gap in `debit` does not mean *"we do not know how much went out"*. It means **nothing went out on this line, because money came in.**

The gap does not represent missing information. **It represents zero.**

> **Fill from meaning, not from habit.** A median debit of \$70 dropped into 565 money-in rows would invent about \$40,000 of payments that never happened.

💻 **The code:**

```python
df = df.fillna({'debit': 0.0, 'credit': 0.0})
```

🔙 That is Week 2's `fillna`, taking a **dictionary** — `{column: value}` — so both columns get handled in one call, each with its own fill.

**Then the second half of this STEP: the rows where nothing happened at all.**

Forty-eight rows have zero on *both* sides. These are the bank's own memo lines — "balance brought forward" and similar. Real rows, no money. They would drag every average towards zero.

To remove them you need a **new operator**. 🔙 Week 2 gave you `&` for AND and `|` for OR. Here is the third:

| Week 1 (single answers) | pandas (whole columns) |
|---|---|
| `and` | `&` |
| `or` | `\|` |
| **`not`** | **`~`** |

```python
df = df[~((df['credit'] == 0) & (df['debit'] == 0))]
#         ^ keep the rows where this is NOT true
```

Read it inside out: *"credit is zero **and** debit is zero"* → *"**not** that"* → *"keep those rows"*.

📺 **Expected output:**

```text
=== STEP 6: WHAT DOES A GAP IN 'DEBIT' ACTUALLY MEAN? ===
Gaps before filling:
debit     565
credit    727
dtype: int64

Think about what the gap MEANS here. Every line of a bank
statement is money in OR money out, never both. A gap in
'debit' does not mean 'we do not know'. It means ZERO --
no money went out on that line, because money came IN.

That is why 0.0 is the honest fill here, and why a median
or a mean would be nonsense.

Gaps after filling:
debit     0
credit    0
dtype: int64

=== STEP 6: THE ROWS WHERE NOTHING HAPPENED ===
Rows with zero on BOTH sides: 48

These are the bank's own memo lines -- 'balance brought
forward' and the like. Real rows, no money. They would drag
every average we calculate towards zero.

Meet a new operator. In Week 2 you learned & for AND and
| for OR. The third one is ~ for NOT:

    df[~((df['credit'] == 0) & (df['debit'] == 0))]
       ^ keep the rows where this is NOT true

Rows before: 1440   after: 1392

And a way to check we removed the right thing -- those memo
lines were the only ones tagged c0:
Rows still tagged c0: 0
Counterparties left:  12
```

**1,440 → 1,392.** Exactly 48 rows gone.

**And now the check that makes this trustworthy.** Those memo lines were the only rows tagged `c0`. After the filter, `c0` rows: **0**. Counterparties: **13 → 12**.

**That is how you verify a filter.** Do not just check that the row count dropped — check that *the thing you meant to remove is gone* and *nothing else went with it*. Anybody can delete 48 rows. Proving they were the right 48 is the job.

⚠️ **Common mistake:** Forgetting the outer brackets around the whole condition: `df[~(df['credit'] == 0) & (df['debit'] == 0)]`. That applies `~` to *only the first condition* and means something entirely different — "credit is not zero AND debit is zero". It runs, it returns rows, and it is wrong. **`~` needs the whole thing in brackets.**

✅ **Verify:** Gaps 565/727 → 0/0, 48 rows removed, 1440 → 1392, `c0` rows 0, 12 counterparties.

🎤 **Try it yourself (60 seconds):** Write the same filter **without** `~`, using `!=` and `|`:

```python
df[(df['credit'] != 0) | (df['debit'] != 0)]
```

Same 1,392 rows. *"NOT (both zero)"* and *"either one is not zero"* are the same statement. Practice problem **p03** proves it properly.

> 📌 **You saw this in class:**
>
> ```python
> # --- Fill NaNs with default values ---
> df.fillna({'debit': 0.0, 'credit': 0.0}, inplace=True)
>
> # --- Remove rows with zero-value transactions ---
> df = df[~((df['credit'] == 0) & (df['debit'] == 0))]
> ```
>
> Identical, `~` and all.

---

### STEP 7 — The imputation rules, for next time

▶ *In your script:* Section 3 of `scripts/05_fill_and_filter.py`

🎯 **Objective:** Learn the general rules, now that you have seen a case that breaks them.

☕ **Story moment:** You just filled with zero because zero was the *meaning*. That will not always be true, so here is what to do the rest of the time.

🧠 **The idea in plain English:** **Imputation** is the proper word for filling in missing values. One rule per column type was given in class:

| Column type | Fill with | Why |
|---|---|---|
| **Numeric** | the **mean** or the **median** | a typical value distorts the column least — and **median when the data is skewed**, which money always is |
| **Categorical** | the **mode** (commonest value), or a label like `"Missing"` | you cannot average the word "transfer" |

**The goal**, in the words used in class: *"maintain data size and prevent loss of information."* Every row you drop is evidence you no longer have. Imputation is how you keep the row when only one cell is damaged.

**And the exception you have just lived through:** when a gap has a **meaning**, use the meaning. Here it meant zero.

**When would you rather drop?** When the row is too damaged to trust — 🔙 like the six mangled dates in STEP 4, where there was nothing honest to guess.

📺 **Expected output:**

```text
=== STEP 7: THE RULES, FOR NEXT TIME ===
A rule was given in class for each kind of column:

  NUMERIC column     -> fill with the mean or the median
                        (median when the data is skewed --
                         which money always is)
  CATEGORICAL column -> fill with the mode, the commonest
                        value, or the label 'Missing'

The goal: keep your data size without inventing signal.
And the exception we just used: when a gap has a MEANING,
use the meaning. Here the meaning was zero.

When would you rather drop? When the row is too damaged to
trust -- like the six mangled dates in STEP 4.
```

**One honest warning to carry with you.** Every imputed value is a **guess that afterwards looks exactly like data**. Nothing in your DataFrame marks it. 🔙 In Lab01 STEP 16 you watched a filled median reappear at hour 5 and pretend to be a finding — that is not a rare accident, that is what imputation *does*. Fill when you must, know how many you filled, and never forget which numbers you made up.

⚠️ **Common mistake:** Reaching for the mean by reflex. On any skewed column — money, delays, incomes, house prices — the mean has already been dragged away from typical by the extremes. **Median is the safer default, and money is always skewed.**

✅ **Verify:** The rules printed. This is a reading STEP.

🎤 **Try it yourself (30 seconds):** What is the **mode** of the `channel` column? `df['channel'].mode()`. That is what you would fill a missing channel with.

---

### 🧠 Quick Quiz #2 — answer from memory, before peeking

**Q1.** Why does `.astype(str)` come first in the cleaning chain?

- A) Because it removes the commas from the numbers
- B) Because it converts the column into numbers immediately
- C) Because it fills the missing values with empty strings
- D) Because `.str` operations only work on text columns

**Q2.** What does `~` do in `df[~((df['credit'] == 0) & (df['debit'] == 0))]`?

- A) It keeps the rows where the condition is NOT true
- B) It deletes the columns named inside the brackets
- C) It converts the condition into a numeric column
- D) It sorts the resulting rows in reverse order

**Q3.** Why fill `debit`'s gaps with `0.0` rather than the median?

- A) Because zero is always the safest fill for any money column
- B) Because the median of this column happens to equal zero
- C) Because a gap here means no money went out — it means zero
- D) Because pandas cannot compute a median on a cleaned column

---

## ☕ Cluster D — What the Money Looks Like

*Scripts for this cluster:* **`scripts/06_chart_money_distributions.py`**, **`scripts/07_chart_balance_over_time.py`**

> ### 📌 Why the charts come *after* the cleaning
>
> Your class notebook charted the money **first** and cleaned it afterwards. We have swapped the order, for the most practical reason there is: **you cannot chart a column you cannot add up.** The class's copy of this data happened to arrive numeric, so charting first worked for them. Ours arrives as text, so cleaning has to come first.
>
> Which is, honestly, the order you will use for the rest of your career.

---

### STEP 8 — Money is always skewed

▶ *In your script:* the whole of `scripts/06_chart_money_distributions.py`

🎯 **Objective:** See the shape of your own money, and recognise skew in the wild.

☕ **Story moment:** 🔙 In Lab01 you met **skew** on flight delays — one tall bar, a long thin tail. Here it is again, on your own bank account, and this time it is a *problem you have to solve* rather than a curiosity.

🧠 **The idea in plain English:** Two histograms side by side, using the same simple layout tool used in class:

```python
plt.subplot(1, 2, 1)   # 1 row, 2 columns, this is chart 1
plt.subplot(1, 2, 2)   # ...and this is chart 2
```

`sns.histplot(..., kde=True)` adds a smooth curve over the bars — the same shape, drawn as a line, which sometimes makes the tail easier to see.

💻 **The code:**

```python
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.histplot(df['debit'], kde=True, color='blue')
plt.title('Money Out (debit)')

plt.subplot(1, 2, 2)
sns.histplot(df['credit'], kde=True, color='green')
plt.title('Money In (credit)')

plt.tight_layout()
plt.savefig("charts/money_distributions.png")
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(data=df[['debit', 'credit']])
plt.savefig("charts/money_boxplot.png")
plt.show()
```

📺 **Expected output:**

```text
=== STEP 8: THE SHAPE OF THE MONEY ===
          debit    credit
count   1387.00   1387.00
mean     228.84    240.23
std     1046.75   1228.14
min        0.00      0.00
25%        0.00      0.00
50%       70.59      0.00
75%      130.66    459.78
max    28500.00  45000.00

Read the debit column: the middle payment is tiny, the mean
is several times bigger, and the max is enormous. That gap
between the middle and the mean is SKEW, and money data
always has it -- a few big payments drag the average up.

Saved charts/money_distributions.png
Saved charts/money_boxplot.png

Both charts are almost unreadable -- everything is squashed
into a stripe at the bottom with a few dots far above.
That is not a broken chart. That is what skew LOOKS like,
and STEP 11 has the fix.
```

**Read the `debit` column of that `describe()` and it tells a very clear story:**

| Row | Value | What it says |
|---|---|---|
| `50%` | **\$70.59** | the typical payment out is about seventy dollars |
| `mean` | **\$228.84** | but the *average* is over three times that |
| `max` | **\$28,500** | because of this |
| `std` | 1,046.75 | four times the mean — enormous spread |

**The median is \$70 and the mean is \$229.** 🔙 Exactly the pattern from Lab01's delays, and the diagnosis is identical: **a handful of very large payments drag the average up while the middle barely moves.**

**And now look at your two charts.** They are almost unreadable. Everything is jammed into a single bar at the far left, with acres of white space and one or two specks near the right edge. The box plot is worse — a flat line at the bottom and dots way above.

**Those charts are not broken. That is what skew looks like when you refuse to do anything about it.** STEP 11 is where you do something about it.

**One number worth explaining.** `count` reads **1,387**, not 1,392. Dropping the six broken dates removed five *more* rows on top of the 48 memo lines — because one of the six broken-date rows *was* a memo line, so it had already gone. **Small discrepancies like that are worth chasing down rather than shrugging at**; it is exactly the habit that catches real bugs.

⚠️ **Common mistake:** Forgetting `plt.figure()` before the second chart. Without it, the box plot draws on top of the histograms and you save the same muddle twice.

✅ **Verify:** `debit` median `70.59` against mean `228.84`, and both PNGs in `charts/`.

🎤 **Try it yourself (60 seconds):** Add a third subplot showing `closing_balance` — `plt.subplot(1, 3, n)` for three across. The balance is *far* less skewed than the transactions, because it is a running total rather than individual events. **Not everything is skewed, and you have to look.**

> 📌 **You saw this in class:**
>
> ```python
> plt.figure(figsize=(12, 6))
>
> plt.subplot(1, 2, 1)
> sns.histplot(df['debit'].dropna(), kde=True, color='blue')
> plt.title('Debit Distribution')
>
> plt.subplot(1, 2, 2)
> sns.histplot(df['credit'].dropna(), kde=True, color='green')
> plt.title('Credit Distribution')
>
> plt.tight_layout()
> plt.show()
>
> plt.figure(figsize=(8, 6))
> sns.boxplot(data=df[['debit', 'credit']])
> plt.title('Boxplot of Debit and Credit')
> plt.show()
> ```
>
> Identical. We dropped the `.dropna()` because by this point there are no `NaN`s left to drop, and added `savefig`.

---

### STEP 9 — The chart with your whole spring in it

▶ *In your script:* the whole of `scripts/07_chart_balance_over_time.py`

🎯 **Objective:** Draw the closing balance over time, and read your own recent history off it.

☕ **Story moment:** This is the chart Mrs Adeyemi will look at first, and possibly the only one she looks at properly. It is also, unexpectedly, rather moving.

🧠 **The idea in plain English:** `sns.lineplot(data=df, x='date', y='closing_balance')` — one line, because the balance is one number that changes over time.

💻 **The code:**

```python
sns.lineplot(data=df, x='date', y='closing_balance', color='purple')
plt.title('The Cozy Bean -- Closing Balance Over 18 Months')
plt.savefig("charts/balance_over_time.png")
plt.show()
```

📺 **Expected output:**

```text
=== STEP 9: THE BALANCE, OVER TIME ===
count     1387.00
mean      6601.56
std       5668.24
min       1615.17
25%       4306.70
50%       5614.12
75%       7276.90
max      52076.55
Name: closing_balance, dtype: float64

Lowest the account ever got:  $ 1615.17
Highest it ever got:          $ 52076.55
Where it finished:            $ 22099.87

It never went negative. For a loan officer, that single fact
is worth more than most of this statement.

=== THE TWO BIGGEST LINES IN 18 MONTHS ===
Biggest money IN:
      date  credit      counterparty  closing_balance
2026-10-16 45000.0 Aperion Bank Loan         48982.56

Biggest money OUT:
      date   debit       counterparty  closing_balance
2026-10-23 28500.0 Northgate Property         23486.52

You know exactly what those two are. One is Mrs Adeyemi's
first tranche landing. The other is the deposit you paid on
the unit two streets over. Your whole spring is those two rows.

Saved charts/balance_over_time.png

Read your chart. Eighteen months of small waves -- takings in,
suppliers and wages out, over and over. Then right at the end,
a cliff UP and a cliff DOWN. Those are the two rows above.
Window closed. Script finished.
```

**Open `charts/balance_over_time.png` and actually look at it.**

Eighteen months of small waves — money in from the till, money out to Beans Direct and Dairy Co and payroll, in and out, week after week, hovering between about \$1,600 and \$8,000. It is the visual signature of a small business that works.

Then, right at the end: **a cliff straight up, and a cliff straight down.**

**\$3,982 → \$48,982** on 16 October. *Mrs Adeyemi's first tranche.*

**\$51,986 → \$23,486** a week later. *The deposit on the unit two streets over.*

**That is your spring, in two rows of a CSV.** Everything before it is the eighteen months of work that earned it.

**And the single most valuable sentence in this entire lab:** *the lowest the account ever got was \$1,615.17.* **It never went negative.** No overdraft, not once, in 548 days. For somebody deciding whether to release the rest of a loan, that one fact carries more weight than any average in this file — because it says *this business does not run out of money*.

⚠️ **Common mistake:** Drawing a line chart while the date column is still text. It "works" — matplotlib plots the strings in file order — but the x-axis becomes 1,387 unreadable labels and any gap in trading is invisible. **The date has to be a real date first**, which is why STEP 4 came before this.

✅ **Verify:** min `1615.17`, max `52076.55`, final `22099.87`, the two named rows, and `charts/balance_over_time.png` on disk.

🎤 **Try it yourself (60 seconds):** Add `df = df[df['date'] < '2026-10-01']` before the chart and rerun. Now you see the eighteen months *without* the two cliffs — and you can finally read the ordinary rhythm, which the cliffs were flattening. **One enormous value can hide everything else on a chart**, which is the exact problem STEP 11 solves with mathematics instead of deletion.

> 📌 **You saw this in class:**
>
> ```python
> plt.figure(figsize=(10, 6))
> sns.lineplot(data=df, x='date', y='closing_balance', color='purple')
> plt.title('Closing Balance Over Time')
> plt.xlabel('Date')
> plt.ylabel('Closing Balance')
> plt.show()
> ```
>
> Identical, plus `savefig`.

---

### 🧠 Quick Quiz #3 — answer from memory, before peeking

**Q1.** `debit` has a median of \$70.59 and a mean of \$228.84. What does that gap tell you?

- A) The column contains errors that need correcting
- B) The column is skewed — a few large payments pull the mean up
- C) The median was calculated on a different set of rows
- D) The column has too many missing values to summarise

**Q2.** Your two histograms were squashed into one bar at the left. Why?

- A) The chart code was missing its `tight_layout()` call
- B) The column still contained text values that could not be drawn
- C) There were too few rows in the data to draw a shape
- D) A few enormous values stretch the axis, flattening everything else

**Q3.** What are the two cliffs at the end of the balance chart?

- A) The loan tranche arriving, and the branch deposit going out
- B) Two payroll runs falling in the same week
- C) The start and the end of the statement period
- D) Two data-entry errors that should be removed

---

## ☕ Cluster E — Outlier, or Loan?

*Script for this cluster:* **`scripts/08_outlier_or_loan.py`**

---

### STEP 10 — The judgement no formula can make

▶ *In your script:* the whole of `scripts/08_outlier_or_loan.py`

🎯 **Objective:** Apply the IQR fence to your own money — and then override what it implies.

☕ **Story moment:** 🔙 Lab01 STEP 13 built the IQR fence on flight delays and flagged 46,178 rows. Now point that exact same code at your own bank account and see what it says.

🧠 **The idea in plain English:** Nothing new — four lines you already wrote yesterday:

```python
Q1 = df['credit'].quantile(0.25)
Q3 = df['credit'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['credit'] < Q1 - 1.5 * IQR) | (df['credit'] > Q3 + 1.5 * IQR)]
```

📺 **Expected output:**

```text
=== STEP 10: THE IQR FENCE, ON YOUR OWN MONEY ===
Q1  = 0.0
Q3  = 459.78
IQR = 459.78
Upper fence (Q3 + 1.5 * IQR) = $1149.44

Credits the formula flags as outliers: 1

      date  credit      counterparty    reference
2026-10-16 45000.0 Aperion Bank Loan TT262893CZ70

=== NOW THE PART NO FORMULA CAN DO ===
The maths flagged exactly one row in eighteen months. And it
is not an error, a typo, or a fraud. It is the single most
important line in the entire file: Mrs Adeyemi's first tranche.

A technique like this was described in class as one that 'identifies outliers and
then removes them'. Do NOT remove this one. If you delete it,
you delete the evidence that the bank already believes in you.

So: FLAG it, explain it, keep it. Add a column saying so.

      date  credit      counterparty  flagged                           flag_reason
2026-10-16 45000.0 Aperion Bank Loan     True large credit - loan tranche, expected

Flagged rows kept in the table: 1
Rows deleted: 0

An outlier is a QUESTION, not a verdict. This one had a
very good answer.

=== ONE MORE, ON THE WAY OUT ===
Debits above the fence ($326.66): 65

Top three:
      date    debit       counterparty
2026-10-23 28500.00 Northgate Property
2025-05-14  4723.87  Cozy Bean Payroll
2025-11-28  4655.57  Cozy Bean Payroll

The branch deposit, and two payroll runs. Every one explainable.
A statement where you can explain every outlier is a statement
a bank can trust.
```

**The formula flagged exactly one row in eighteen months.** And it is **the loan tranche.**

**Stop and appreciate what just happened.** A completely blind statistical rule, which knows nothing about coffee or banks or you, reached into 1,387 transactions and put its finger on **the single most important line in the file.** That is outlier detection working *perfectly*.

**And now the part that matters more than any of the arithmetic.**

Of this technique, class said: *"This technique first identifies outliers and then removes them."*

**Do not remove this one.**

If you delete that row because a formula flagged it:

- your total money-in drops by \$45,000
- the two cliffs vanish from your balance chart
- the evidence that **the bank already believes in you** disappears from your own evidence pack
- and you hand Mrs Adeyemi a document that fails to mention the money she personally sent you

> ## An outlier is a **question**, not a verdict.
>
> The question is always *"why is this here?"* Sometimes the answer is "a typo" and you fix it. Sometimes it is "a sensor broke" and you drop it. And sometimes it is **"because that is the most important thing that happened all year"** — and then you *flag it, explain it, and keep it.*

So the script adds two columns — `flagged` and `flag_reason` — and **deletes nothing**. Rows deleted: **0**. That is a real technique, not a dodge: the outlier is now marked, the reason travels with the data, and the next person to read it has your reasoning instead of a mystery.

**Then the same fence on the way out**, where 65 debits are flagged: the branch deposit, and every payroll run. **All explainable.** And that is the actual test:

> **A statement where you can explain every outlier is a statement a bank can trust.**

⚠️ **Common mistake:** Reading `Q1 = 0.0` as an error. It is not — **more than a quarter of the rows have zero in `credit`**, because they are money-*out* rows. On a column that is mostly zeros, the quartiles sit at zero, and the fence lands somewhere unexpected. **The fence formula does not know your column is half zeros.** You do.

✅ **Verify:** Exactly `1` credit outlier, and it is `Aperion Bank Loan` on 2026-10-16. Rows deleted: `0`.

🎤 **Try it yourself (60 seconds):** Run the fence on `closing_balance` instead. How many rows get flagged, and what are they? *(The post-tranche week — because for seven days you were carrying \$50,000. Also completely explainable.)*

---

## ☕ Cluster F — Reshaping Numbers

*Scripts for this cluster:* **`scripts/09_chart_log_transform.py`**, **`scripts/10_one_hot_channel.py`**, **`scripts/11_scaling_by_hand.py`**

---

### STEP 11 — Squash the giants, lift the crowd

▶ *In your script:* the whole of `scripts/09_chart_log_transform.py`

🎯 **Objective:** Apply a log transform safely, and see what it does to a skewed column.

☕ **Story moment:** STEP 8 left you with two unreadable charts. Here is the fix, and it is one function call — with one trap you must step around first.

🧠 **The idea in plain English:** A **logarithm** answers: *"what power do I raise the base to, to get this number?"* With base 10, the log of 100 is 2, because 10² = 100. `np.log` uses a slightly different base — a mathematician's constant called *e*, about 2.718 — which changes the numbers but not the behaviour. And the behaviour is the point: it compresses big numbers far more than small ones:

| Value | `np.log(value)` |
|---|---|
| 100 | 4.61 |
| 1,000 | 6.91 |
| 28,500 | 10.26 |

100 → 28,500 is a **285-fold** jump. Logged, 4.61 → 10.26 is barely **double**. It was put well in class: the log transform *"handles skewed data, makes the distribution more approximately normal"* and *"reduces the effects of outliers through normalisation of magnitude differences"*.

**Nothing is deleted and no order changes.** The biggest payment is still the biggest. It just stops shouting.

### ⚠️ And now the trap

**You cannot take the logarithm of zero.** There is no power you can raise 10 to and get 0.

After STEP 6, **600 of your 1,387 rows have `debit` exactly 0.00** — every money-in row. Log the column as it stands and numpy tells you off:

```text
RuntimeWarning: divide by zero encountered in log
0        -inf
1        -inf
2    5.719361
3    4.194341

min: -inf
mean: -inf
How many broken values? 600
```

**Look at what `-inf` does.** It is not a small number, it is a **broken** number, and it spreads: the column's `min` is `-inf`, its `mean` is `-inf`, and any histogram of it is unplottable. **600 poisoned values from one missing filter.**

**The fix is one line.** 🔙 Week-2 boolean filtering — keep only the rows where money actually moved:

💻 **The code:**

```python
payments = df.loc[df['debit'] > 0, 'debit']
logged = np.log(payments)
```

**One plain-English sentence for why:** *you cannot take the log of zero, so we log only the rows where money actually moved.*

That is not a workaround — it is the *correct* statement of the question. "What does a typical payment look like?" was never a question about the rows that were not payments.

📺 **Expected output:**

```text
=== STEP 11: THE ZERO PROBLEM ===
Rows where debit is exactly 0.00: 600 of 1387

Those are the money-IN rows -- nothing went out, so debit is
zero. And you cannot take the logarithm of zero. There is no
power you can raise 10 to and get 0.

Ask numpy anyway and it warns you, then hands back -inf,
which poisons every chart it touches. So we filter first.

=== ONLY THE ROWS WHERE MONEY ACTUALLY MOVED ===
Real payments out: 787
count      787.00
mean       403.31
std       1364.42
min         45.01
25%         85.60
50%        121.12
75%        170.38
max      28500.00
Name: debit, dtype: float64

=== THE SAME PAYMENTS, LOGGED ===
count    787.0000
mean       5.0089
std        0.9757
min        3.8069
25%        4.4497
50%        4.7968
75%        5.1381
max       10.2577
Name: debit, dtype: float64

Before: smallest $45.01, biggest $28500.00 -- a 633x spread.
After:  smallest 3.81, biggest 10.26 -- a 2.7x spread.

Nothing was deleted and no order changed. The biggest payment
is still the biggest. We just stopped it shouting.

Saved charts/log_transform.png

Left: one tall bar at the far left, empty space, a speck.
Right: an actual shape you can read. Same payments, both times.
THAT is what the log transform is for.
```

**A 633× spread becomes 2.7×.** And now open `charts/log_transform.png` and compare the two panels:

- **Left (raw):** one tall bar at the far left, a lot of white space, a speck near the right edge.
- **Right (logged):** an actual hump you can read, with a visible spread and a tail.

**Same 787 payments. Same order. Same information.** One picture is unusable and the other tells you what a typical Cozy Bean payment looks like. That is the whole technique.

⚠️ **Common mistake:** Logging a column with zeros in it and not checking. It **warns** rather than crashing, and a `RuntimeWarning` in a wall of output is desperately easy to miss. Then your mean is `-inf` and you spend an hour wondering why. **Filter first, and check your min afterwards.**

✅ **Verify:** 600 zeros, 787 real payments, logged min `3.8069` and max `10.2577`, no infinities, and `charts/log_transform.png` on disk.

🎤 **Try it yourself (60 seconds):** Remove the `.loc[...]` filter and log the whole column. Read the `RuntimeWarning`. Look at `logged.min()` and `logged.mean()`. **Meet this bug on purpose now** rather than by accident at 11pm.

> 📌 **You saw this in class:** the only `np.log` call there was carefully guarded too —
>
> ```python
> if ratio <= 0 or np.isnan(ratio) or np.isinf(ratio):
>     log_balance = 0
> else:
>     log_balance = np.log(abs(ratio))
> ```
>
> Different guard, same instinct: **never hand `np.log` a value you have not checked.** Class teaches the log transform as a technique but never ran it on a raw money column, so this STEP is that technique made concrete on data where it matters.

> ### 🚀 Bonus — beyond class: `np.log1p`, the version that survives a zero
>
> There is another way round the zero problem: **`np.log1p(x)` computes `log(1 + x)`**. Feed it zero and you get `log(1) = 0.0` — no warning, no `-inf`, no filter needed:
>
> ```python
> logged = np.log1p(df['debit'])      # every row, no guard
> print("Any infinities?", bool(np.isinf(logged).any()))    # False
> ```
>
> **So why not always use it?** Because it quietly changes what the numbers *mean*. `log1p(0)` is `0.0` — the same answer it would give a real \$0 payment. STEP 11's filter says *"those rows are not payments at all"* and leaves them out; `log1p` says *"those rows are payments of zero"* and keeps them.
>
> **Both are defensible. Just know which question you asked.** Practice 🚀 p09 runs both side by side.

---

### STEP 12 — Words a machine can add up

▶ *In your script:* the whole of `scripts/10_one_hot_channel.py`

🎯 **Objective:** One-hot encode a categorical column and read a row of it aloud.

☕ **Story moment:** The `channel` column says how each payment moved: `card`, `cash`, `transfer`, `standing_order`. Useful to you, useless to a model. **You cannot multiply the word "transfer" by anything.**

🧠 **The idea in plain English:** **One-hot encoding** turns one text column into **several 0/1 columns — one per value**, each answering a yes/no question.

From class: it *"converts categorical data into a form ML algorithms can understand"* and *"enables grouping of categorical data without losing any information, creating binary (0/1) features for each category."*

**"Without losing any information"** is the important claim. Before: one column, four possible words. After: four columns, each 0 or 1, exactly one of them a 1. Nothing lost, nothing invented.

💻 **The code:**

```python
dummies = pd.get_dummies(df['channel'], prefix='channel')
dummies = dummies.astype(int)
df = pd.concat([df, dummies], axis=1)
```

📺 **Expected output:**

```text
=== STEP 12: THE COLUMN THAT IS STILL WORDS ===
How did the money move?
channel
transfer          692
card              564
standing_order     78
cash               53
Name: count, dtype: int64

Four values, all text. A model cannot add up the word
'transfer'. So we turn one text column into several
number columns -- one per value, each answering yes or no.

=== ONE LINE LATER ===
New columns: ['channel_card', 'channel_cash', 'channel_standing_order', 'channel_transfer']

pandas hands them to you as True/False:
   channel_card  channel_cash  channel_standing_order  channel_transfer
0          True         False                   False             False
1         False          True                   False             False
2         False         False                   False              True
3         False         False                   False              True
4         False         False                   False              True

...and .astype(int) turns those into the 0s and 1s your
class describes. Same information, easier to read:
   channel_card  channel_cash  channel_standing_order  channel_transfer
0             1             0                       0                 0
1             0             1                       0                 0
2             0             0                       0                 1
3             0             0                       0                 1
4             0             0                       0                 1

=== READ ROW 2 OUT LOUD ===
The original value was: 'transfer'
channel_card              0
channel_cash              0
channel_standing_order    0
channel_transfer          1

In English: 'this transaction was NOT card, NOT cash,
NOT a standing order, and YES a transfer.'
Exactly one 1 per row. That is why it is called ONE-hot.

=== THE COST, STATED PLAINLY ===
Columns before encoding: 9
Columns after encoding:  12

Four new columns for four values. That is fine. But imagine
one-hot encoding a column with 500 counterparty names --
you would get 500 columns. That is the trade-off, and it is
why you encode the small columns and think hard about the big ones.
```

**Read row 2 out loud, because that is when it clicks:**

> *"This transaction was **not** card, **not** cash, **not** a standing order, and **yes** a transfer."*

**Exactly one `1` per row.** One value is "hot". That is where the name comes from, and once you have said it aloud once you will never need it explained again.

**Two things worth knowing beyond the mechanics:**

**1. pandas gives you `True`/`False`, not `1`/`0`.** Class promises "binary (0/1) features", and `.astype(int)` delivers exactly that. The information is identical either way — 🔙 Python has always treated `True` as 1 — but 0s and 1s are easier to read in a wide table and are what every textbook shows.

**2. The cost is columns, and it can get out of hand.** Four values gave four new columns, taking the table from 9 to 12. Fine. But one-hot encoding `counterparty` — or a real customer-name column with 500 values — would give you **500 columns**, mostly zeros. **That is why you encode the small categorical columns and think hard about the big ones.**

⚠️ **Common mistake:** One-hot encoding an **identifier** rather than a category. `counterparty_id` has 12 values here and would "work" — but IDs are labels, not categories, and encoding them tells a model that being counterparty 7 is a *property* you could share with somebody else. Encode `channel` (a genuine category). Leave IDs alone.

✅ **Verify:** Four new columns, exactly one `1` per row, and 9 → 12 columns.

🎤 **Try it yourself (60 seconds):** Run `dummies.sum()`. The column totals — 564, 53, 78, 692 — are the same numbers as `value_counts()` at the top, just alphabetical instead of biggest-first. **That is your check that the encoding invented nothing and lost nothing.** Practice p05 makes you prove it two ways.

---

### STEP 13 — Two rulers for one column

▶ *In your script:* the whole of `scripts/11_scaling_by_hand.py`

🎯 **Objective:** Scale a column two ways with plain arithmetic — and recognise one of the formulas.

☕ **Story moment:** Last technique from class, and it is the one where Week 1 comes back and takes a bow.

🧠 **The idea in plain English:** From class: *"Numerical features often do not have a common range and differ from each other (e.g. age vs income). Scaling solves this by making continuous features identical in terms of range."*

The problem, in your own data:

- `debit` runs from **45.01** to **28,500.00**
- `closing_balance` runs from **1,615.17** to **52,076.55**

Some algorithms treat a bigger number as a **more important** number, purely because it is bigger. Scaling stops that. Two ways:

**Normalisation (min-max)** — squeeze everything into 0…1:

```text
scaled = (x - min) / (max - min)
```

**Standardisation (z-score)** — centre on 0, measure in standard deviations:

```text
scaled = (x - mean) / std
```

💻 **The code — no new functions at all:**

```python
lo, hi = payments.min(), payments.max()
minmax = (payments - lo) / (hi - lo)

mean, std = payments.mean(), payments.std()
zscores = (payments - mean) / std
```

📺 **Expected output:**

```text
=== STEP 13: WHY SCALE ANYTHING? ===
Two of our columns, side by side:
  debit           runs from      45.01 to    28,500.00
  closing_balance runs from   1,615.17 to    52,076.55

Same units, wildly different ranges. Some algorithms treat a
bigger number as a more important number, purely because it
is bigger. Scaling stops that.

=== NORMALISATION (MIN-MAX): PUT EVERYTHING IN 0 TO 1 ===
    scaled = (x - min) / (max - min)

min = 45.01
max = 28,500.00

First five payments, before and after:
   original   min_max
2    304.71  0.009127
3     66.31  0.000749
4    110.16  0.002290
5   1850.00  0.063433
6    100.04  0.001934

Smallest becomes exactly 0.0, largest exactly 1.0.
Every other payment lands somewhere in between. That is all it does.

=== STANDARDISATION (Z-SCORE): CENTRE ON ZERO ===
    scaled = (x - mean) / std

mean = 403.311004
std  = 1,364.418057

First five payments, before and after:
   original   z_score
2    304.71 -0.072266
3     66.31 -0.246992
4    110.16 -0.214854
5   1850.00  1.060297
6    100.04 -0.222271

New mean: 0.000000   new std: 1.000000
Centred on zero, one standard deviation wide. By construction.

=== YOU HAVE ALREADY DONE THIS ===
Look at that second formula again:  (x - mean) / std

That is EXACTLY the z-score you worked out by hand for one
late flight in Lab01 STEP 14. Same arithmetic, same two
ingredients. There it was a way to spot a weird value. Here
it is a way to prepare a column for a model.

One formula, two jobs. Week-1 arithmetic IS ML preprocessing.

Who cares about this? K-means, linear regression and neural
networks all behave badly on unscaled columns. Names only
for now -- you meet them in Module 2.
```

> ### 🔙 **Stop. Look at that second formula again.**
>
> ```text
> (x - mean) / std
> ```
>
> **That is the z-score you worked out by hand in Lab01 STEP 14** for a Hawaiian Airlines flight that left 853 minutes late. Same subtraction. Same division. Same two ingredients out of `describe()`.
>
> In Lab01 it was a way to **spot a weird value** — *"this flight is 21 standard deviations out"*.
>
> Here it is a way to **prepare a column for a model** — *"put this column on a standard ruler"*.
>
> **One formula. Two completely different jobs.** Nobody told you yesterday that you were learning a machine-learning preprocessing step. You were.

**And notice the two rulers answer different questions**, which is how you choose between them:

- **Min-max** always gives you exactly **0.0** and **1.0** at the ends. Useful when you need a guaranteed range. It says *"this was the largest one"*.
- **Z-score** always gives you **mean 0, std 1**. Useful when you care how *unusual* a value is. It says *"this is eight standard deviations above normal"* — which is a much more interesting sentence.

**Who cares?** Class names three: **K-means**, **linear regression**, **neural networks**. All three behave badly on unscaled columns. Names only today — Module 2 is where you meet them.

⚠️ **Common mistake:** Scaling using the **whole** dataset's min/max/mean when you will later split into training and test sets. That leaks information from the test set into your preparation — a real and famous mistake. Not something you can trip over today, but worth knowing the phrase **data leakage** before somebody says it to you.

✅ **Verify:** min-max min `0.0` and max `1.0`; z-score mean `0.000000` and std `1.000000`.

🎤 **Try it yourself (60 seconds):** Find the z-score of the biggest payment: `zscores.max()`. About **20.6** — the \$28,500 branch deposit sits twenty standard deviations above a typical Cozy Bean payment. 🔙 **The same method that flagged the Hawaiian flight just flagged your branch deposit.** Two labs, one formula.

---

### 🧠 Quick Quiz #4 — answer from memory, before peeking

**Q1.** Why must you filter before taking `np.log` of the `debit` column?

- A) Because the column contains commas that numpy cannot read
- B) Because the column is skewed and needs sorting first
- C) Because log of zero is undefined and produces `-inf`
- D) Because `np.log` only accepts one value at a time

**Q2.** The IQR fence flagged the \$45,000 loan tranche. What should you do?

- A) Flag it, explain it, and keep it in the data
- B) Delete it, because outliers distort every average
- C) Replace it with the median credit value
- D) Split it into smaller amounts across several rows

**Q3.** What does a log transform do to a skewed column?

- A) It removes the largest values from the column entirely
- B) It compresses large values more than small ones, without reordering
- C) It converts the column into categories a model can read
- D) It fills the column's missing values with the geometric mean

---

### 🧠 Quick Quiz #5 — answer from memory, before peeking

**Q1.** One-hot encoding `channel` (4 values) produced what?

- A) One column containing the numbers 1 to 4
- B) Four rows, one for each channel type
- C) One column of True/False for the commonest channel
- D) Four columns of 0s and 1s, exactly one 1 per row

**Q2.** What is the difference between min-max and z-score scaling?

- A) Min-max works on text columns; z-score needs numbers
- B) Min-max removes outliers; z-score keeps them
- C) Min-max lands in 0…1; z-score centres on mean 0, std 1
- D) They produce identical results on any numeric column

**Q3.** Which algorithms were named in class as caring about scale?

- A) K-means, linear regression and neural networks
- B) Decision trees, random forests and boosting
- C) Only deep neural networks with many layers
- D) None — scaling is purely for human readability

---

## ☕ Cluster G — Building the Features

*Scripts for this cluster:* **`scripts/12_features_totals.py`**, **`scripts/13_features_calendar.py`**

---

### STEP 14 — Named aggregations: money in, money out

▶ *In your script:* Section 1 of `scripts/12_features_totals.py`

🎯 **Objective:** Build your first two real features with a named aggregation.

☕ **Story moment:** The statement has 1,387 rows. Mrs Adeyemi does not want 1,387 rows. She wants **one row per counterparty** — *who pays you, who you pay, and how much.*

🧠 **The idea in plain English:** 🔙 Week 2's `groupby` deals the rows into piles. What is new is how you say what you want from each pile:

```python
totals = (
    df.groupby('counterparty_id', as_index=False)
      .agg(
          total_debit=('debit', 'sum'),
          total_credit=('credit', 'sum'),
      )
)
```

**Read that middle line once and you own it for life:**

```text
total_debit = ('debit', 'sum')
     ^            ^        ^
new column    old column  what to do to it
```

This is a **named aggregation**. You *name the column you want* and say how to build it. 🔙 In Week 2 you used `agg({'total_bill': ['mean', 'sum']})`, which gave you that two-level header you had to squint at. The named form gives you **plain, flat, properly-named columns** instead — and it is what was used in class itself.

`as_index=False` keeps `counterparty_id` as a normal column instead of moving it into the index. One less thing to think about later.

📺 **Expected output:**

```text
=== STEP 14: FEATURES 1 AND 2 -- THE TOTALS ===
One row per counterparty. Who pays us, who we pay.

counterparty_id  total_debit  total_credit
             c1         0.00     271116.53
            c10         0.00      17086.67
            c11      1128.76          0.00
            c12      2346.06          0.00
             c2     31682.99          0.00
             c3     31272.79          0.00
             c4     25901.43          0.00
             c5    158770.11          0.00
             c6     33300.00          0.00
             c7      4503.62          0.00
             c8         0.00      45000.00
             c9     28500.00          0.00

Read the syntax once and you own it for life:
    total_debit=('debit', 'sum')
     ^new column   ^old column  ^what to do to it

This is a NAMED aggregation. You name the column you want
and say how to build it. No two-level headers, no flattening.
```

**Twelve rows. That is your whole business.**

And look at the shape of it — **every counterparty is either all-debit or all-credit, never both.** `c1` only ever pays you; `c5` you only ever pay. That is not a coincidence, it is what a bank statement *is*: money comes from customers and goes to suppliers. **Your feature table has already discovered the structure of your business** and you have written two lines.

✅ **Verify:** Twelve rows, `c1` with `total_credit` 271116.53, `c8` with 45000.00.

🎤 **Try it yourself (30 seconds):** Add `biggest_single=('debit', 'max')` to the `agg(...)` call. One more feature, one more line. **That is how a feature table grows.**

> 📌 **You saw this in class:**
>
> ```python
> result = (
>     df.groupby('customer_id', as_index=False)
>       .agg(
>           total_debit=('debit', 'sum'),
>           total_credit=('credit', 'sum')
>       )
> )
> ```
>
> **Identical** — we group by `counterparty_id` where the class grouped by `customer_id`, because our rows are the Cozy Bean's counterparties rather than a bank's customers.

---

### STEP 15 — Three more features, three different ways

▶ *In your script:* Sections 2–3 of `scripts/12_features_totals.py`

🎯 **Objective:** Build features 3, 4 and 5 — and notice that not all of them need a `groupby`.

☕ **Story moment:** Two features down. Mrs Adeyemi's questions are not finished.

🧠 **The idea in plain English:** Three more, and the interesting part is that they come from **different places**:

**Feature 3 — `net_position`.** *"Overall, did money flow towards us or away from us?"* This one needs **no groupby at all** — it is arithmetic on two columns you already built. 🔙 Exactly like `per_cup` in STEP 2.

```python
totals['net_position'] = totals['total_credit'] - totals['total_debit']
```

**Feature 4 — `mean_debit`.** *"What does a typical payment to them look like?"* Another named aggregation, `'mean'` instead of `'sum'`.

**Feature 5 — `txn_count`.** *"How often do we deal with them?"* `('reference', 'count')` — counting a column that is never empty gives you the number of rows in each pile.

📺 **Expected output:**

```text
=== STEP 15: FEATURE 3 -- NET POSITION ===
A column built from two other columns. No groupby needed --
just arithmetic, exactly like Week 1.

=== STEP 15: FEATURES 4 AND 5 -- AVERAGE AND COUNT ===
counterparty_id         counterparty  total_debit  total_credit  net_position  mean_debit  txn_count
             c1      Card Settlement         0.00     271116.53     271116.53        0.00        546
            c10         Cash Deposit         0.00      17086.67      17086.67        0.00         53
            c11    Card Machine Fees      1128.76          0.00      -1128.76       62.71         18
            c12 Insurance & Licences      2346.06          0.00      -2346.06      391.01          6
             c2     Beans Direct Ltd     31682.99          0.00     -31682.99      189.72        167
             c3             Dairy Co     31272.79          0.00     -31272.79      104.94        298
             c4    Muffin Top Bakery     25901.43          0.00     -25901.43      115.12        225
             c5    Cozy Bean Payroll    158770.11          0.00    -158770.11     4410.28         36
             c6   Riverside Lettings     33300.00          0.00     -33300.00     1850.00         18
             c7           City Power      4503.62          0.00      -4503.62      250.20         18
             c8    Aperion Bank Loan         0.00      45000.00      45000.00        0.00          1
             c9   Northgate Property     28500.00          0.00     -28500.00    28500.00          1

=== WHAT THESE FIVE COLUMNS ALREADY TELL MRS ADEYEMI ===
  Our biggest source of money: Card Settlement ($271,116.53)
  Our biggest cost:            Cozy Bean Payroll ($158,770.11)
  Who we deal with most often: Card Settlement (546 transactions)

Five columns. Twelve rows. That is a business, described.

HONESTLY, THOUGH: the class notebook built 45 of these in one
giant 100-line loop. That is a working data scientist's version
of exactly what you just did by hand -- same idea, more of it.
You are not doing a simplified version. You are doing the
readable version.
```

**Read that table as the owner of the business, not as a student.** It is genuinely the shape of the Cozy Bean:

- **\$271,116** came in from card settlements over 18 months, across **546** separate days.
- **\$158,770** went out in wages — your biggest single cost by a wide margin. That is Sara, Ben and Aisha, paid fortnightly for eighteen months, and it is worth seeing written down: **your largest expense is your people.**
- **Riverside Lettings** took exactly **\$1,850, eighteen times.** A perfectly flat `mean_debit` with 18 transactions is the signature of a **standing order** — you can see the *rent* in the numbers without being told.
- **c9, Northgate Property:** one transaction, `mean_debit` **\$28,500**. When count is 1, the mean *is* the payment. That is the branch deposit.
- **Beans Direct** got 167 payments averaging \$190; **Dairy Co** got 298 averaging \$105. Milk more often, beans in bigger batches. **That is your supply chain, visible in two columns.**

### 🫱 And now the honest bit about the class notebook

The class notebook built **45 features** in a single loop of about a hundred lines — quarterly windows, fortnightly windows, standard deviations, ratios, counts of counts.

**That is a working data scientist's version of exactly what you just did.** Same `groupby`, same aggregations, same idea — just forty-five of them at once, in a loop too dense to read while you are still learning what a feature *is*.

**You are not doing a simplified version. You are doing the readable version**, one feature at a time, understanding each one. When you meet that 100-line loop in a real codebase — and you will — you will recognise every move in it.

⚠️ **Common mistake:** Using `('debit', 'count')` and expecting the number of *payments*. `count` counts **non-null** values, and after STEP 6 every `debit` is non-null — the zeros count too. So `('debit', 'count')` gives you the pile size, same as `('reference', 'count')`. To count actual payments you need `(df['debit'] > 0).sum()`. **`count` counts rows that have a value, not rows you find interesting.**

✅ **Verify:** Twelve rows, seven columns, `c5` `mean_debit` `4410.28`, `c6` exactly `1850.00`.

🎤 **Try it yourself (60 seconds):** Sort by `txn_count` descending. Who do you deal with most after Card Settlement? *(Dairy Co, 298 times — milk arrives more often than anything else. Obvious once you see it, invisible in 1,387 raw rows.)*

---

### STEP 16 — The three features that need a calendar

▶ *In your script:* the whole of `scripts/13_features_calendar.py`

🎯 **Objective:** Build features 6, 7 and 8 out of the date column — and avoid a bug that is in the class notebook.

☕ **Story moment:** Five features describe *how much*. Mrs Adeyemi also wants *how often* and *how recently* — and those live in the date column.

🧠 **The idea in plain English:**

**Feature 6 — `active_days`.** `('date', 'nunique')` counts **different** dates. Five transactions on one day is **one** active day. That is a rhythm, not a total.

**Feature 7 — `busiest_day`.** 🔙 STEP 4's real dates unlock `.dt`, and `.dt.day_name()` gives you `"Monday"` from a timestamp. *(This is the class's "encoding cycles — day-of-week" made concrete.)*

Then, per counterparty, the commonest day. `value_counts()` sorts biggest-first, and **`.idxmax()` gives the label with the biggest count** — the winner's *name*, not the number of times it won. We use a 🔙 Week-1 `for` loop over the groups, because "the commonest value in this pile" reads clearest that way:

```python
rows = []
for cp_id, group in df.groupby('counterparty_id'):
    day_counts = group['day_name'].value_counts()
    rows.append({'counterparty_id': cp_id, 'busiest_day': day_counts.idxmax()})
busiest = pd.DataFrame(rows)
```

🔙 A list, a dictionary and a `for` loop — three Week-1 ideas building a feature table.

**Feature 8 — `days_since_last_txn`.** *"How recently did we last hear from them?"* And this one contains a trap.

💻 **The code:**

```python
REVIEW_DATE = pd.Timestamp("2026-11-06")

recency = df.groupby('counterparty_id', as_index=False).agg(last_txn_date=('date', 'max'))
recency['days_since_last_txn'] = (REVIEW_DATE - recency['last_txn_date']).dt.days
```

Subtracting two dates gives a **Timedelta** — a duration — and `.dt.days` pulls the whole number of days out of it.

📺 **Expected output:**

```text
=== FEATURE 6 -- HOW MANY DIFFERENT DAYS? ===
counterparty_id  active_days
             c1          546
            c10           53
            c11           18
            c12            6
             c2          154
             c3          258
             c4          199
             c5           36
             c6           18
             c7           18
             c8            1
             c9            1

'nunique' counts DIFFERENT values. Five transactions on one
day is one active day. This is a rhythm, not a total.

=== FEATURE 7 -- WHICH DAY OF THE WEEK? ===
A whole new column, out of thin air:
      date day_name     counterparty
2025-05-01 Thursday  Card Settlement
2025-05-01 Thursday     Cash Deposit
2025-05-01 Thursday Beans Direct Ltd

Across the whole statement, our busiest weekday is:
day_name
Friday       204
Monday       201
Wednesday    200
Saturday     198
Sunday       197
Tuesday      194
Thursday     193
Name: count, dtype: int64

And per counterparty:
counterparty_id busiest_day
             c1    Thursday
            c10     Tuesday
            c11      Sunday
            c12      Friday
             c2      Monday
             c3      Friday
             c4   Wednesday
             c5   Wednesday
             c6    Thursday
             c7     Tuesday
             c8      Friday
             c9      Friday

.idxmax() means 'the label with the biggest count' -- the
winner's NAME, not the number of times it won.

=== FEATURE 8 -- HOW RECENTLY? ===
Measuring everything against the review date: 2026-11-06

counterparty_id last_txn_date  days_since_last_txn
             c1    2026-10-31                    6
            c10    2026-10-31                    6
            c11    2026-10-25                   12
            c12    2026-08-08                   90
             c2    2026-10-28                    9
             c3    2026-10-29                    8
             c4    2026-10-31                    6
             c5    2026-10-28                    9
             c6    2026-10-01                   36
             c7    2026-10-20                   17
             c8    2026-10-16                   21
             c9    2026-10-23                   14

=== WHY THE REFERENCE DATE HAS TO COME FROM OUTSIDE ===
Suppose we had measured 'days since last transaction' against
each counterparty's OWN last transaction. Watch what happens:

  days_since_last_txn would be: [0]

Zero. Every time. For everybody. Because you asked how long
it has been since the last day... measured from the last day.

The class notebook has exactly this bug, and its version of
this feature reads 0 for every single customer. A feature that
is the same for every row tells a model NOTHING.

So a recency feature always needs a fixed outside date:
today, the application date, or -- as here -- the review date.
```

**Look at `c2` and `c3`. Both are suppliers, both got about 30 grand.** But `c2` (beans) has **154 active days** across 167 transactions, and `c3` (milk) has **258** across 298. `active_days` separates two counterparties that `total_debit` made look identical. **That is what a feature is for.**

And `c12` — Insurance & Licences — was last paid **90 days ago**. Everybody else is within about three weeks. That is not a problem, it is a *quarterly bill*, and the recency feature spotted it without being told.

> ### ⚠️ Feature 8's trap, and it is in your class notebook
>
> This is worth reading twice.
>
> The class notebook computes this feature like so:
>
> ```python
> today = account_df['date'].max()          # the group's own latest date
> last_txn_date = account_df['date'].max()  # ...the same thing again
> days_since_last_transaction = (today - last_txn_date).days
> ```
>
> Both sides are `account_df['date'].max()`. **So the answer is always exactly 0**, for every customer, in every row — as the script demonstrates above by reproducing it: `[0]`.
>
> **A feature that has the same value for every row carries no information whatsoever.** It is a column of zeros wearing a useful-sounding name, and because it has a plausible name it can survive in a codebase for a very long time before anybody checks.
>
> **The fix is to measure against a fixed date from outside the data** — today, the application date, or here the **review date, 2026-11-06**. That is why `REVIEW_DATE` is a constant at the top of the script rather than something computed from `df`.
>
> **And the transferable lesson:** after you build any feature, look at its values. If they are all the same, you have not built a feature. `df['my_feature'].nunique()` takes two seconds and would have caught this.

⚠️ **Common mistake:** Subtracting dates and expecting a number. `REVIEW_DATE - last_txn_date` gives a **Timedelta** like `6 days 00:00:00`. It prints oddly and does not compare to integers the way you expect. **`.dt.days` is what turns it into 6.**

✅ **Verify:** `c1` 546 active days, `c12` 90 days since last, and the broken version printing `[0]`.

🎤 **Try it yourself (60 seconds):** Check the class's bug on your own table: `print(recency['days_since_last_txn'].nunique())`. You should get 9 or so different values — a real feature. Then compute the broken version and check *its* `nunique()`. **You get 1.** That single number is how you catch a dead feature.

---

## ☕ Cluster H — Meet Merge

*Script for this cluster:* **`scripts/14_meet_merge.py`**

---

### STEP 17 — Stapling two tables together

▶ *In your script:* the whole of `scripts/14_meet_merge.py`

🎯 **Objective:** Join two summary tables on a shared key, and understand `how='left'`.

☕ **Story moment:** You now have features arriving in several small batches — money features from STEP 15, calendar features from STEP 16. They need to be **one table** before they can be one page.

🧠 **The idea in plain English:** **`pd.merge` staples two tables together side by side, matching rows by a shared column.**

That shared column is called the **key**. Here it is `counterparty_id`, which appears in both tables.

```python
merged = pd.merge(totals, counts, on='counterparty_id', how='left')
```

- **`on='counterparty_id'`** — the key to match on
- **`how='left'`** — **"keep every row from the LEFT table, and bring over matches from the right."** The left table is the one you named first.

📺 **Expected output:**

```text
=== STEP 17: TWO TABLES, ONE SHARED COLUMN ===

TABLE A -- the money (first four rows):
counterparty_id  total_debit  total_credit
             c1         0.00     271116.53
            c10         0.00      17086.67
            c11      1128.76          0.00
            c12      2346.06          0.00

TABLE B -- the activity (first four rows):
counterparty_id  txn_count  active_days
             c1        546          546
            c10         53           53
            c11         18           18
            c12          6            6

Both have a 'counterparty_id' column. That shared column is
the KEY, and it is what lets us staple them together.

=== ONE LINE ===
    merged = pd.merge(totals, counts, on='counterparty_id', how='left')

counterparty_id  total_debit  total_credit  txn_count  active_days
             c1         0.00     271116.53        546          546
            c10         0.00      17086.67         53           53
            c11      1128.76          0.00         18           18
            c12      2346.06          0.00          6            6
             c2     31682.99          0.00        167          154
             c3     31272.79          0.00        298          258
             c4     25901.43          0.00        225          199
             c5    158770.11          0.00         36           36
             c6     33300.00          0.00         18           18
             c7      4503.62          0.00         18           18
             c8         0.00      45000.00          1            1
             c9     28500.00          0.00          1            1

Table A had 3 columns. Table B had 3.
The merged table has 5 -- the key is not repeated.
Rows: 12 in, 12 out. Nothing lost.

=== WHAT how='left' MEANS ===
'Keep every row from the LEFT table, and bring over matches
from the right.' The left table is the one you named first.

It matters when the right table is missing somebody. Watch:

Table B with c8 (the loan) deliberately removed, then merged:
counterparty_id  total_debit  total_credit  txn_count  active_days
             c8          0.0       45000.0        NaN          NaN

c8 survived -- because it was in the left table -- but its
right-hand columns are NaN. how='left' keeps the row and admits
it does not know. That is usually exactly what you want, and
it is why a merge can quietly introduce new gaps.

Always check isna().sum() after a merge. Always.
Gaps introduced by that merge: 2
```

**3 columns + 3 columns = 5 columns**, because the key is not repeated. **12 rows in, 12 rows out.** Nothing lost, nothing duplicated.

**Then the demonstration that actually teaches `how='left'`.** The script deliberately removes `c8` — the loan — from the right-hand table and merges again. And `c8` **survives**, with `NaN` in its right-hand columns.

**That is the promise of `how='left'`, stated exactly:** *keep every row on the left; where the right has nothing to offer, admit it with `NaN` rather than dropping the row.*

Usually that is exactly what you want. **But look at the last line: the merge introduced 2 new gaps.** You had a clean table, you merged, and now you have `NaN`s that were not there before — and pandas did not warn you, because nothing went wrong.

> ## Always check `isna().sum()` after a merge. Always.
>
> A merge that silently fails to match is one of the most common ways a real analysis goes quietly wrong. The row count looks right, the columns look right, and a third of your values are `NaN` because the key had trailing spaces in one table.

⚠️ **Common mistake:** Merging on a key that is not unique in the right-hand table. If the right table has `c1` twice, `c1` comes out of the merge **twice** — and your 12-row table becomes 13 rows without a word of complaint. **Check `merged.shape[0]` against what you expected**, every time. Duplicated rows from a bad merge silently inflate every total you compute afterwards.

✅ **Verify:** 5 columns, 12 rows in and out, and the `c8` demo showing `NaN` with 2 gaps introduced.

🎤 **Try it yourself (60 seconds):** Change `how='left'` to `how='inner'` in the c8 demonstration. Now `c8` **vanishes entirely** — `inner` keeps only rows present in *both* tables. **You just lost the loan tranche from your evidence pack by changing one word.** That is why `how` is worth understanding rather than copying.

> 📌 **You saw this in class:**
>
> ```python
> merged_df = pd.merge(result_df, totals, on='customer_id', how='left')
> final_df = pd.merge(merged_df, features_df, on='customer_id', how='left')
> ```
>
> **Identical form** — the class stapled three tables into one with two merges, on `customer_id`. Ours joins on `counterparty_id` because that is our key.

---

## ☕ Cluster I — The Evidence Pack

*Script for this cluster:* **`scripts/15_evidence_pack.py`**

---

### STEP 18 — What a junior data analyst hands a loan officer

▶ *In your script:* the whole of `scripts/15_evidence_pack.py`

🎯 **Objective:** Assemble every feature into one table, save it, and write the page that goes on top.

☕ **Story moment:** Thursday evening. The review is on the 6th. This is the envelope.

🧠 **The idea in plain English:** Nothing new — the whole lab, in order:

1. **clean** — STEPs 4–6
2. **build every feature** — STEPs 14–16, in one named aggregation plus one loop
3. **merge** — STEP 17
4. **save the machine-readable table** — `engineered_counterparties.csv`
5. **write the human-readable page** — 🔙 Week-1 f-strings and `open()`

📺 **Expected output:**

```text
=== THE ENGINEERED FEATURE TABLE ===
counterparty_id         counterparty  total_debit  total_credit  mean_debit  txn_count  active_days  net_position  days_since_last_txn busiest_day
             c1      Card Settlement         0.00     271116.53        0.00        546          546     271116.53                    6    Thursday
             c8    Aperion Bank Loan         0.00      45000.00        0.00          1            1      45000.00                   21      Friday
            c10         Cash Deposit         0.00      17086.67        0.00         53           53      17086.67                    6     Tuesday
            c11    Card Machine Fees      1128.76          0.00       62.71         18           18      -1128.76                   12      Sunday
            c12 Insurance & Licences      2346.06          0.00      391.01          6            6      -2346.06                   90      Friday
             c7           City Power      4503.62          0.00      250.20         18           18      -4503.62                   17     Tuesday
             c4    Muffin Top Bakery     25901.43          0.00      115.12        225          199     -25901.43                    6   Wednesday
             c9   Northgate Property     28500.00          0.00    28500.00          1            1     -28500.00                   14      Friday
             c3             Dairy Co     31272.79          0.00      104.94        298          258     -31272.79                    8      Friday
             c2     Beans Direct Ltd     31682.99          0.00      189.72        167          154     -31682.99                    9      Monday
             c6   Riverside Lettings     33300.00          0.00     1850.00         18           18     -33300.00                   36    Thursday
             c5    Cozy Bean Payroll    158770.11          0.00     4410.28         36           36    -158770.11                    9   Wednesday

Shape: 12 counterparties x 10 features

Saved engineered_counterparties.csv

================================================================
   THE COZY BEAN -- EVIDENCE PACK FOR FULL DISBURSEMENT
   Prepared for: Mrs Adeyemi   |   Review date: 2026-11-06
================================================================

1. WHAT THIS IS BUILT FROM
   Bank statement, 2025-05-01 to 2026-10-31.
   1440 statement lines received; 1387 real transactions after
   cleaning (6 unreadable dates dropped, 48 memo lines removed).

2. THE HEADLINE NUMBERS
   Money in over the period:   $  333,203.20
   Money out over the period:  $  317,405.76
   Net movement:               $   15,797.44
   Lowest balance reached:     $    1,615.17
   Closing balance:            $   22,099.87
   The account never went overdrawn.

3. THE TWO LARGEST MOVEMENTS, EXPLAINED
   2026-10-16  +$45,000.00  Aperion Bank Loan
      -> your first tranche, received and held.
   2026-10-23  -$28,500.00  Northgate Property
      -> deposit paid on the branch-two unit.
   Both are flagged as statistical outliers and both are
   expected. Nothing has been removed from this data.

4. WHO WE TRADE WITH
   12 counterparties over 18 months.
   9 of them are net outflows (suppliers, staff, rent, utilities).
   Three largest costs:
      Cozy Bean Payroll      $ 158,770.11  (36 payments)
      Riverside Lettings     $  33,300.00  (18 payments)
      Beans Direct Ltd       $  31,682.99  (167 payments)

5. THE FEATURE TABLE
   Attached: engineered_counterparties.csv
   12 rows x 10 columns -- eight engineered features
   per counterparty: totals in and out, net position, average
   payment, transaction count, active days, busiest weekday,
   and days since last activity at the review date.

PREPARED BY: the owner, The Cozy Bean
STATUS: full disbursement pending your review.
================================================================

Saved evidence_pack.txt

Two files. One a machine can read, one a person can read.
That is what a junior data analyst hands a loan officer.
Three weeks ago you had never written a line of Python.
```

**Read section 1 of that note again, because it is the most professional thing in this entire lab:**

> *1,440 statement lines received; 1,387 real transactions after cleaning (6 unreadable dates dropped, 48 memo lines removed).*

**You told her what you threw away, and why.** Not "here are my numbers" — *"here are my numbers, here is what I removed to get them, and here is how many."* Anybody can produce a total. Producing a total **with its provenance attached** is what makes it evidence rather than an assertion.

**And section 3 does the same for the outliers:** both flagged, both explained, *"nothing has been removed from this data."* 🔙 That is STEP 10's judgement call, written down where the person making the decision can see it.

**Two files come out of this, and they are for two different readers:**

| File | Reader | Why it exists |
|---|---|---|
| `engineered_counterparties.csv` | a **machine** — or a bank analyst who wants to sort it | 12 rows × 10 features, ready for anything |
| `evidence_pack.txt` | **Mrs Adeyemi** | so a human being can understand it in ninety seconds |

Producing only the CSV would be a student's answer. Producing only the note would be a shopkeeper's. **Producing both is the job.**

⚠️ **Common mistake:** Shipping a feature table with no documentation of how it was built. In six months you will not remember that `days_since_last_txn` was measured against 6 November, and a number whose definition you have forgotten is worse than no number. **The note is not decoration — it is the definition.**

✅ **Verify:** `engineered_counterparties.csv` (12 rows × 10 columns) and `evidence_pack.txt` both exist in your lab folder. **Open them both.**

🎤 **Try it yourself (5 minutes):** Add a sixth section to the note: **"6. WHAT I WOULD WANT TO SEE NEXT."** What would *you* ask for if you were Mrs Adeyemi and this landed on your desk? Write two sentences. **Knowing the limits of your own analysis is the most senior skill in this lab.**

---

### 🧠 Quick Quiz #6 — answer from memory, before peeking

**Q1.** In `agg(total_debit=('debit', 'sum'))`, what is `'debit'`?

- A) The name of the new column being created
- B) The existing column the calculation reads from
- C) The name of the aggregation function to apply
- D) The value to fill missing entries with

**Q2.** What does `how='left'` keep?

- A) Only rows that appear in both tables being joined
- B) Only rows unique to the left-hand table
- C) Every row from the left table, plus matches from the right
- D) Every row from both tables, filling gaps with zeros

**Q3.** Why must a "days since last transaction" feature use an outside reference date?

- A) Because pandas cannot subtract two dates in the same column
- B) Because the review date is always later than the data
- C) Because timedeltas need a fixed anchor to convert to days
- D) Because measuring from the group's own last date always gives 0

---

## 5. 🏋️ Practice Problems

**How practice works here:** one problem per file in `practice/`; run just the one you want. Every file's header repeats the task **and the exact expected output**. Every file runs as-is before you touch it. Answers are in `solutions/` — **open them only after a genuine attempt.**

| # | File | Story task | You will practise |
|---|---|---|---|
| p01 | `p01_open_the_statement.py` | Describe what the bank sent before fixing any of it. | `shape`, `select_dtypes`, `nunique` |
| p02 | `p02_clean_one_column.py` | The third money column is still text. Fix it from memory. | ⭐ the four cleaning beats |
| p03 | `p03_the_not_filter.py` | Write the same filter twice — with `~`, and without it. | `~`, `&`, `\|`, `!=` |
| p04 | `p04_log_the_payments.py` | Log the **credit** column, and get the guard right. | `.loc` filter, `np.log`, `np.isinf` |
| p05 | `p05_one_hot_the_channel.py` | Encode the channel — then **prove** your encoding is correct. | `get_dummies`, `sum(axis=1)` |
| p06 | `p06_scale_by_hand.py` | Scale the balance both ways, with Week-1 arithmetic only. | min-max, z-score |
| **p07** | `p07_a_function_that_features.py` | **You have read that nine-line cleaning block eight times. Write it ONCE.** | ⭐ 🔙 **Week-1 `def`**, named agg |
| **p08** | `p08_capstone_evidence_pack.py` | **CAPSTONE — Mrs Adeyemi asks a different question: is this business *steady*?** | ⭐ the whole lab |
| 🚀 p09 | `p09_bonus_log1p_and_shares.py` | **Bonus:** `np.log1p`, and counting money versus counting things. | bonus material only |

> 🚀 **p09 is a bonus** and uses `np.log1p` and `value_counts(normalize=True)`, neither of which was in your class session. **Nothing depends on it.**

### 🏔️ About the two big ones

**p07 is the payoff for a deliberate irritation.** Every script from 06 onwards repeats the same nine lines of cleaning. That was on purpose — so each script runs standalone, and so that by now you are thoroughly sick of reading it. **p07 is where that irritation becomes a function.** Repetition is the signal that a function is missing, and noticing it is a professional instinct rather than a complaint.

**p08 asks a question this walkthrough never asked.** Script 15 built one row per *counterparty* — "who do we trade with?". Mrs Adeyemi's next question is *"is this business steady?"*, which is a question about **time**, so a row must mean **a month**.

Nothing about the code changes much. **What changes is what a row means** — and choosing that is the first and most important decision in feature engineering. Get it wrong and every clever thing you do afterwards answers the wrong question beautifully.

---

## 6. 📚 Cheat Sheet & Glossary

- **[CHEATSHEET.md](CHEATSHEET.md)** — ⭐ **the cleaning & feature recipes.** The four-move string chain, the imputation rules, the log guard, one-hot, both scaling formulas, named aggregations and merge. **This is the page you will still be using in a year.**
- **[GLOSSARY.md](GLOSSARY.md)** — feature, feature engineering, imputation, encoding, one-hot, scaling, normalisation, standardisation, log transform, aggregation, key, merge and the rest, one friendly line each.

*(Lab01's [cheat sheet](../Lab01/CHEATSHEET.md) covers the profiling and EDA half of this week, and both still apply.)*

---

## 7. 🤔 Reflection (2 minutes — please actually do this)

1. **Which judgement call did you find hardest?** Fill or drop? Flag or delete? Log or leave? There is no formula for any of them, and that is why the job exists.
2. **What is still fuzzy?** Name the one thing you would ask an instructor sitting beside you. Write it down.
3. **Find your own \N.** Export something from a real system in your life — a bank statement, a payment app, a spreadsheet somebody else maintains. Open it with `read_csv` and run `info()`. **How many of its columns are text that ought to be numbers?** You now have the four moves that fix them.
4. **And one to sit with:** you spent most of today cleaning rather than analysing. That ratio is not a flaw in this lab. **That ratio is the job.**

---

## 8. ✅ Answer Key

*No peeking until you have answered. Eighteen questions in total.*

### Quiz #1

| Q | Answer | Why |
|---|---|---|
| 1 | **B** — a column holding one useful fact | Rows are observations, columns are features. A is the definition of an observation. |
| 2 | **C** — writes `NaT` where a date cannot be read, without crashing | That is exactly what `coerce` buys you: countable failures instead of a traceback. It does not drop the rows — you do that yourself. |
| 3 | **A** — nothing can be added up until they are converted | `.sum()` on a text column glues values together instead of adding them. There are usable values in there; they are just wearing the wrong costume. |

### Quiz #2

| Q | Answer | Why |
|---|---|---|
| 1 | **D** — `.str` operations only work on text columns | Without it you get `AttributeError: Can only use .str accessor with string values`. It costs nothing and makes the next three beats safe. |
| 2 | **A** — keeps the rows where the condition is NOT true | `~` is pandas' `not`, alongside `&` for and and `\|` for or. |
| 3 | **C** — a gap here means no money went out, so it means zero | Fill from **meaning**, not from habit. The median (\$70) would invent about \$40,000 of payments that never happened. |

### Quiz #3

| Q | Answer | Why |
|---|---|---|
| 1 | **B** — the column is skewed; large payments pull the mean up | Median \$70.59, mean \$228.84, max \$28,500. The same pattern as Lab01's flight delays. |
| 2 | **D** — a few enormous values stretch the axis | The \$28,500 deposit forces the x-axis wide, squashing 780-odd ordinary payments into one bar. STEP 11 fixes it. |
| 3 | **A** — the loan tranche in, and the branch deposit out | +\$45,000 on 16 October and −\$28,500 on the 23rd. Your whole spring in two rows. |

### Quiz #4

| Q | Answer | Why |
|---|---|---|
| 1 | **C** — log of zero is undefined and produces `-inf` | 600 rows have `debit` of exactly 0. Unguarded, you get a `RuntimeWarning` and 600 `-inf` values that poison the mean and the chart. |
| 2 | **A** — flag it, explain it, keep it | Deleting it would remove the most important row in the file. An outlier is a question, not a verdict. |
| 3 | **B** — compresses large values more than small ones, without reordering | A 633× spread becomes 2.7×. Nothing is deleted and the biggest payment is still the biggest. |

### Quiz #5

| Q | Answer | Why |
|---|---|---|
| 1 | **D** — four columns of 0s and 1s, exactly one 1 per row | One column per value, one "hot" value per row. That is where the name comes from. |
| 2 | **C** — min-max lands in 0…1; z-score centres on mean 0, std 1 | Different rulers for different questions: "the largest one" versus "eight standard deviations out". |
| 3 | **A** — K-means, linear regression and neural networks | Named in class as sensitive to feature magnitude. Tree-based methods (B) largely are not. |

### Quiz #6

| Q | Answer | Why |
|---|---|---|
| 1 | **B** — the existing column the calculation reads from | The pattern is `new_name=('old_column', 'function')`. A describes `total_debit`; C describes `'sum'`. |
| 2 | **C** — every row from the left table, plus matches from the right | Where the right table has no match, you get `NaN` — which is why you check `isna().sum()` after every merge. A describes `how='inner'`. |
| 3 | **D** — measuring from the group's own last date always gives 0 | Exactly the bug in the class notebook: both sides were `account_df['date'].max()`, so every customer scored 0. A feature identical for every row carries no information. |

---

## 9. ➡️ What's Next

Look at what you did today.

You were handed a file in which **every single column was text** — money with commas in it, `\N` where values should be, the word `None` leaked into a CSV, six dates that were not dates, and forty-eight rows where nothing happened at all. You could not add up a column of it.

By this evening you have: **cleaned it in four deliberate moves**, decided what its gaps *meant* rather than what a rule said, removed 48 rows and **proved you removed the right 48**, found the one statistical outlier in eighteen months and **correctly refused to delete it**, compressed a 633-fold spread into something a human can read, **encoded** words into numbers, **scaled** a column two ways, engineered **eight features** one at a time, **merged** two tables on a key, and shipped **two files** — one for a machine, one for Mrs Adeyemi.

And somewhere in the middle you noticed that `(x - mean) / std` — the z-score you worked out by hand yesterday for a Hawaiian Airlines flight — turns out to be a **machine-learning preprocessing step.** Same arithmetic. Completely different job. That is what this week has been doing to you the whole time.

**Three weeks ago you had never written a line of Python.** This week you profiled a third-of-a-million-row dataset, scraped the live internet, and engineered features for a loan decision.

**You are not learning to be an analyst any more. You did analyst work today.**

**Next module** the models arrive. And here is the thing worth knowing before they do: **every one of them starts with a table exactly like the one you built this afternoon.** `pd.read_csv`, then `info()`, then a long careful look, then the cleaning, then the features. The clever algorithm at the end is the short part. **What you did today is the part that decides whether the clever bit learns anything real** — which is why "garbage in, garbage out" was worth its own STEP.

The three processes from STEP 2 were **data preparation → EDA → benchmark**. You have now done the first two properly, twice. **Benchmark is Module 2**, and you will arrive there able to build the table it needs.

The evidence pack is in the envelope. Mrs Adeyemi reviews it on the 6th.

The second branch opens in the spring. ☕

---

*Apeiron AI Training Academy · Module 1: AI/ML Fundamentals · Week 3 · Lab02*
*"Boundless Possibilities, Infinite Potential"*
