This folder is where your charts land.

It ships almost empty on purpose -- every PNG in here is one YOU
made by running a script. Nothing in this folder is shipped with
the lab except this note.

By the end of the walkthrough you should have four of them:

  money_distributions.png    STEP 8   -- debit and credit, side by side
  money_boxplot.png          STEP 8   -- both columns in one box plot
  balance_over_time.png      STEP 9   -- 18 months, and the two cliffs
  log_transform.png          STEP 11  -- before and after, same payments

The one to actually look at is balance_over_time.png. Eighteen
months of small waves, then a cliff up and a cliff down: the loan
tranche arriving on 2026-10-16, and the deposit on the branch-two
unit going out a week later. Your whole spring, in one line chart.

Two rules for every chart script in this lab:

  1. os.makedirs("charts", exist_ok=True) FIRST -- matplotlib will
     not create this folder for you, and savefig into a folder that
     does not exist raises FileNotFoundError.

  2. plt.savefig(...) BEFORE plt.show() -- on many setups, showing
     a figure clears it, and then you save a blank PNG.

And one extra, because this lab draws two charts in some scripts:
call plt.figure() between them, or the second draws on top of the
first and you save the same muddle twice.
