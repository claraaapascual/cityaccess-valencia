from pathlib import Path
import os
import runpy
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
os.chdir(REPO_ROOT)
sys.path.insert(0, str(REPO_ROOT))

runpy.run_path(str(REPO_ROOT / "app.py"), run_name="__main__")
