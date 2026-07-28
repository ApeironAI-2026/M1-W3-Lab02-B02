# ============================================================
#  The Cozy Bean -- Script 00: Check Your Setup
#  Run this FIRST, before anything else in this lab.
#
#  Week 2 checked five libraries. This week there are SIX --
#  google-play-scraper is the one new install.
#  Nothing here can break anything; run it as often as you like.
#
#  Run:   python scripts/00_check_setup.py  (from M1-W3-Lab02/)
# ============================================================

import sys
import importlib.metadata

# Make sure the tick and cross below can always be printed, on
# every computer and every terminal.
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

print("=== THE COZY BEAN -- KITCHEN INSPECTION (WEEK 3) ===")
print()

# (name to import, name to type at pip, name on PyPI)
libraries = [
    ("pandas", "pandas", "pandas"),
    ("numpy", "numpy", "numpy"),
    ("matplotlib", "matplotlib", "matplotlib"),
    ("seaborn", "seaborn", "seaborn"),
    ("scipy", "scipy", "scipy"),
    ("google_play_scraper", "google-play-scraper", "google-play-scraper"),
]

all_good = True

for import_name, pip_name, dist_name in libraries:
    try:
        module = __import__(import_name)
        # Most libraries carry their own __version__. google_play_scraper
        # does not, so we ask the installer instead.
        version = getattr(module, "__version__", None)
        if version is None:
            version = importlib.metadata.version(dist_name)
        print(f"  ✅  {import_name:20} {version}")
    except ImportError:
        all_good = False
        print(f"  ❌  {import_name:20} NOT INSTALLED")
        print(f"        try:  py -m pip install {pip_name}")

print()

if all_good:
    print("All six ready. You can start the lab.")
else:
    print("Something is missing -- see the line marked above.")
    print("Install it, then run this script again.")
