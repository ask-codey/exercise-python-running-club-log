# Exercise: Running Club Log

Exercise code for the lesson **Exercise: Running Club Log** in the Python in Depth course on [ask-codey.com](https://www.ask-codey.com).

The Riverbend Running Club keeps its runs in a spreadsheet saved as a CSV file, and each member's weekly goal in a JSON file. You'll write the five functions in `club.py` that read the runs, total each runner's miles, write a summary CSV, and save and load the goals. Tests call each function and check what it returns or writes.

## What's here

- `club.py`: the five functions, `read_runs`, `miles_by_runner`, `write_summary`, `save_goals` and `load_goals`. Each one stops with `NotImplementedError: Not built yet.` for now. The docstring under each says what it should do, with examples. For you to finish.
- `report.py`: prints the club's week with your five functions and writes `summary.csv`, so you can see them at work. Ready to use.
- `runs.csv`: the week's runs, one per line under the header `date,runner,miles,minutes`. `report.py` reads it.
- `goals.json`: each member's weekly goal in miles. `report.py` reads it.
- `tests/test_club.py`: tests that call your functions and check what comes back. You don't need to change this file.
- `requirements.txt`: the one package the tests need, pytest, at an exact version. Ready to use.
- `pytest.ini`: tells pytest where the tests are and where to find `club.py`. Ready to use.
- `.gitignore`: tells Git to leave out the virtual environment, the files Python and pytest make as they run, and the two files `report.py` writes. Ready to use.

The tests and `report.py` bring your functions in with an `import` line, such as `from club import read_runs`.

## Before you start

The tests need pytest, and pytest goes in a virtual environment: a private set of packages for this folder only. In VS Code's terminal, in this folder, run these three commands.

On Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

On a Mac (zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- The first command makes the virtual environment, in a folder named `.venv`.
- The second turns it on for this terminal: the prompt starts with `(.venv)` from then on.
- The third installs the packages `requirements.txt` lists into it: here, only pytest.

*Virtual Environments and pip* explains all three. The `.venv` folder is in `.gitignore`, so Git leaves it out: these commands make it again on any computer.

If PowerShell answers that running scripts is disabled on this system, run this once, then run the second command again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Each new terminal starts with the virtual environment off. If the prompt doesn't start with `(.venv)`, run the second command again. (VS Code often turns it on for you.)

## Check your work

```bash
pytest
```

At first every test fails: that is expected, because each function stops with a `NotImplementedError` for now. Each function you finish turns its tests green. A failing test's message says what it called, what it expected and what came back, for example *read_runs on a runs.csv holding only the header should return [], but it returned None.*

The tests never touch your own files. Each test writes the small files it needs into `tmp_path`, an empty folder pytest makes for that test alone, and hands your function that folder's path. A path pytest makes isn't text, but `open()` takes it as it is, so pass `path` straight to `open()`.

To see your functions at work, run this from the exercise folder, so it finds `runs.csv` and `goals.json`:

```bash
python report.py
```

## The rules

- Keep each function's name and parameters as they are.
- Open every file with `encoding="utf-8"`, and every CSV file with `newline=""` as well.
- Read and write CSV with the `csv` module, and JSON with the `json` module; both are already imported at the top of `club.py`.
- Return each answer from `read_runs`, `miles_by_runner` and `load_goals`; don't print it.
- Don't change the tests, `report.py`, `runs.csv` or `goals.json`.

## Tips

- `csv.DictReader` gives each row as a dictionary keyed by the header's column names, with every value as text: `float()` and `int()` turn the numbers into numbers.
- `csv.DictWriter` needs `fieldnames`, then `writeheader()` once and `writerow()` for each row.
- `totals.get(runner, 0)` gives a runner's total so far, or 0 for a runner you haven't seen yet.
- `json.dump(goals, file, indent=2)` saves the goals, and `json.load(file)` reads them back.
- A missing file stops `open()` with a `FileNotFoundError`. `try` and `except FileNotFoundError` let `load_goals` return `{}` instead.

## Hand it in

When it works, push your solution to a public repo of your own on GitHub, then paste that repo's address into **Submit your exercise** on the lesson page at [ask-codey.com](https://www.ask-codey.com). That's what completes the lesson. The lesson page shows the Git commands, step by step.
