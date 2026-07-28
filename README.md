# ☕ M1-W3-Lab02 — The Evidence Pack: Turning a Bank Statement into Features

**Aperion AI Training Academy** · *"Boundless Possibilities, Infinite Potential"*

| | |
|---|---|
| **Module** | M1: AI/ML Fundamentals |
| **Week** | Week 3 |
| **Lab** | Lab02 — The Evidence Pack |
| **Topic** | Feature engineering · imputation · outlier treatment · log transform · one-hot encoding · scaling · named aggregations · `pd.merge` |
| **Duration** | **≈ 1 hour** of lab work, **plus ~10 minutes of setup** |
| **Difficulty** | ⭐⭐⭐ Beginner, level 3 — **you speak pandas now** |

Mrs Adeyemi released the first tranche and wants one more thing before signing off the rest: *"I need to see how the business **behaves**, not just what it **earned**."* There is exactly one document that answers that, and you have been avoiding it for eighteen months because it is unbearable to look at — **the bank statement**, 1,440 rows of `\N`, `NaN`, comma-riddled numbers and dates stored as text.

This lab turns it into features a decision can rest on.

**Start here → [`M1-W3-Lab02.md`](M1-W3-Lab02.md)** — the full lab, with quizzes and an answer key.

> 🎁 **Nothing new to install this week.** If you did Lab01, you are already set up.

---

## 1. 📥 Get this repo onto your computer

You reached this repo by clicking the **GitHub Classroom link posted in Google Classroom**. That link made **your own private copy** of the lab — the URL has your GitHub username in it. This is the copy you clone.

### 1.1 Where to put it

This is a **separate repo** from Week 3 Lab01, so it gets its own folder right next to it:

```text
AperionAI/
└── Module1/
    ├── Week1/
    │   ├── Lab01/
    │   └── Lab02/
    ├── Week2/
    │   ├── Lab01/
    │   └── Lab02/
    └── Week3/
        ├── Lab01/      ← already cloned
        └── Lab02/      ← this repo goes here
```

**Keep `AperionAI` out of OneDrive, iCloud Drive, Google Drive and Dropbox** — this lab writes PNG charts, and a syncing folder can lock a file mid-write.

### 1.2 Copy your repo's address

Click the green **`< > Code`** button, select the **HTTPS** tab, and click the 📋 copy icon. You get something like `https://github.com/AperionAI-2026/M1-W3-Lab02-B02-<your-username>.git`. **Use your own address**, not a classmate's.

### 1.3 Clone it into `Week3/Lab02`

**Windows (PowerShell):**

```text
cd ~\AperionAI\Module1\Week3
git clone PASTE-YOUR-REPO-URL-HERE Lab02
cd Lab02
```

**Mac / Linux:**

```text
cd ~/AperionAI/Module1/Week3
git clone PASTE-YOUR-REPO-URL-HERE Lab02
cd Lab02
```

That last word — `Lab02` — names the folder.

> **Folder `Week3` does not exist yet?** You have not cloned Lab01. Create it with `mkdir -Force ~\AperionAI\Module1\Week3` (Windows) or `mkdir -p ~/AperionAI/Module1/Week3` (Mac), then clone.

Then confirm:

```text
pwd
ls
```

`pwd` must end in **`Week3/Lab02`**. `ls` must show `README.md`, `M1-W3-Lab02.md`, `CHEATSHEET.md`, `GLOSSARY.md`, `data`, `charts`, `scripts`, `practice` and `solutions`.

---

## 2. 🔧 Setup — about 10 minutes

**If you did Lab01 today**, you are already set up. Open your `Lab02` folder (**File → Open Folder…**), open a terminal, and run:

```text
py scripts/00_check_setup.py
```

Six ✅ ticks and you are away.

**If you are starting fresh:**

```text
py -m pip install pandas matplotlib seaborn scipy google-play-scraper
py scripts/00_check_setup.py
```

On **Mac**, or if `py` is not recognised, use `python3 -m pip install …` and `python3 scripts/…`. Whichever prefix you pick, use it for *everything* in this lab.

| What you see | What to do |
|---|---|
| `'pip' is not recognized…` (Windows) | Use `py -m pip install …` — this asks *Python* to run pip, which always works. |
| `SSL: CERTIFICATE_VERIFY_FAILED` or it hangs on "Collecting…" | Try home wifi first. **If you have PostgreSQL installed**, a stale `CURL_CA_BUNDLE` variable may be the cause — in PowerShell run `$env:CURL_CA_BUNDLE = $null` for that terminal, then retry. |
| `Successfully installed` but still `ModuleNotFoundError` | You have more than one Python. Use the same prefix for both the install and the run. |

---

## 3. 📂 What is in this repo

| Path | What it is |
|---|---|
| [`M1-W3-Lab02.md`](M1-W3-Lab02.md) | **The lab.** Quizzes, capstone, answer key. |
| [`CHEATSHEET.md`](CHEATSHEET.md) | Every call from this lab on one page. Print it. |
| [`GLOSSARY.md`](GLOSSARY.md) | Plain-English definitions of the new words. |
| `data/cozybean_statement.csv` | **1,440 rows** of deliberately messy bank statement — the whole point of the lab. |
| `charts/` | **Starts almost empty on purpose.** Your PNGs land here. |
| `scripts/` | `00_check_setup.py` plus fifteen numbered scripts. |
| `practice/` | Nine practice problems, including the capstone evidence pack. **Your code goes here.** |
| `solutions/` | Worked solutions. Have a real go first. |

> 🛋️ **Aim for one sitting of about an hour.** If you do need to pause, the natural break is after **Cluster C**, when the statement is finally clean. Everything before that break is repair work; everything after is building.

---

## 4. 💾 Saving your work back to GitHub

From inside `Lab02`, when you finish, or any time you pause:

```text
git add .
git commit -m "Cleaned the statement"
git push
```

Your PNG charts in `charts/` get committed too — deliberately. They are evidence of your own work.

---

## 5. 🆘 If something goes wrong

| What you see | What it means | What to do |
|---|---|---|
| `FileNotFoundError: … 'data/cozybean_statement.csv'` | 🔙 Wrong folder. | `pwd` must end in `Lab02`. `ls` must show `data`. If not: **File → Open Folder** on your `Lab02` folder, then a fresh terminal. |
| **The terminal froze after a chart appeared** | It has not. It is waiting for you to close the chart window — **which may be hiding behind VS Code** | Find it, admire it, close it. **Your PNG was already saved** before the window opened. |
| **Output did not change after an edit** | **The file was never saved.** | Look for the ● dot on the file tab. **Ctrl+S** / **Cmd+S**. Rerun. |

Still stuck after a genuine try? Post in the course channel with **what you ran**, **what you expected**, and **the last line of the error**.

---

*Aperion AI Training Academy · Module 1, Week 3, Lab 02 · Previous: [Lab01 — Due Diligence](https://github.com/AperionAI-2026/M1-W3-Lab01-B02)*
