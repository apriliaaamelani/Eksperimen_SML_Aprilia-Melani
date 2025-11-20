**Purpose**
- **Goal**: Help AI coding agents become productive quickly in this repository: data-preparation and exploratory modeling for a diabetes dataset.

**Quick Start**
- **Open data**: primary raw data is at `diabetes_raw/diabetes.csv`.
- **Run preprocessing script**: (script is empty at present) but the notebook demonstrates the intended preprocessing steps. To run the notebook interactively use Jupyter: `jupyter lab` or `jupyter notebook` and open `preprocessing/Eksperimen_Aprilia-Melani.ipynb`.
- **Run automation**: if `preprocessing/automate_Aprilia-Melani.py` is implemented, run `python preprocessing/automate_Aprilia-Melani.py` from repository root using PowerShell.

**Project Layout (important files)**
- **`diabetes_raw/diabetes.csv`**: source dataset used by notebooks and scripts.
- **`preprocessing/Eksperimen_Aprilia-Melani.ipynb`**: canonical exploratory notebook — inspect it first to learn conventions and typical transformations.
- **`preprocessing/automate_Aprilia-Melani.py`**: intended automation script (currently empty). Prefer to mirror notebook logic here when implementing.

**Key Patterns & Conventions (from the notebook)**
- **Relative paths**: code uses relative paths (example: `file_path = "../diabetes_raw/diabetes.csv"` inside the notebook). Always resolve relative paths with respect to the notebook/script working directory.
- **Stateful notebook variables**: the notebook refers to variables like `df`, `df_clean`. Before saving or referencing a DataFrame ensure the variable is defined (the last cell attempts to save `df_clean` but the notebook's earlier cells define `df`). Verify the correct variable to persist.
- **Preprocessing steps to mirror in scripts**: drop duplicates, clip outliers (example: `df['bmi']=df['bmi'].clip(lower_bound,upper_bound)`), `LabelEncoder` for `gender` and `smoking_history`, correlation inspection, and `train_test_split(..., random_state=42)` for reproducibility.
- **Output artifact**: expected saved output path in the notebook is `../preprocessing/diabetes_preprocessing.csv` — agents should keep this output path consistent when creating automation.

**Dependencies**
- Primary Python libs used in the notebook: `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn` (`LabelEncoder`, `train_test_split`), and `warnings`.
- Use a virtual environment and pin versions when adding `requirements.txt`. Minimal example: `numpy, pandas, matplotlib, seaborn, scikit-learn`.

**Common Gotchas / Checks for the agent**
- **Undefined variable**: verify `df_clean` exists before `to_csv`. If not present, default to saving `df` or create `df_clean` by applying the notebook's cleaning steps.
- **Relative path confusion**: when running scripts from repository root, the notebook's `../` patterns may behave differently; canonicalize paths using `Path(__file__).resolve().parent` in scripts.
- **Empty automation script**: `preprocessing/automate_Aprilia-Melani.py` is currently empty — when implementing, port notebook cells (data load -> clean -> encode -> save) and provide a `--input`/`--output` CLI.

**Editing & Testing workflow**
- **Iterate in the notebook**: open `preprocessing/Eksperimen_Aprilia-Melani.ipynb` to explore transformations and generate a script from working cells.
- **Implement script**: create `main()` and argument parsing; add a reproducible `random_state=42` and logging prints for key steps.
- **Run quick smoke tests**: `python -c "import pandas as pd; print(pd.read_csv('preprocessing/diabetes_preprocessing.csv').shape)"` after saving to confirm output.

**When to ask the user**
- If required behavior is ambiguous (e.g., which DataFrame variable to persist, expected schema changes), ask for intended canonical variable names and desired output schema.

**Merging guidance (if an existing Copilot instructions file exists)**
- Preserve any project-specific commands. Prefer the notebook as the source-of-truth for preprocessing examples. If merging, add or update the "Common Gotchas" and "Key Patterns" sections using concrete examples from the latest notebook cells.

If you'd like, I can: implement `preprocessing/automate_Aprilia-Melani.py` by porting the notebook, or open a PR with the scripted preprocessing and a `requirements.txt`.
