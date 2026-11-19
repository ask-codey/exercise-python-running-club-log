"""The Riverbend Running Club's log: five functions for you to finish.

The docstring under each function says what it should do, with examples.
Replace each raise NotImplementedError("Not built yet.") line with your own
code. Open every file with encoding="utf-8", and every CSV file with
newline="" as well. Each path is the file's name or a path to it: pass it to
open() as it is.
"""
import csv
import json


def read_runs(path):
    """Return the runs in the CSV file at path, as a list of dictionaries.

    The file's header is date,runner,miles,minutes. Each run becomes one
    dictionary with those four keys, in the file's order. Convert the miles
    to a float and the minutes to an int; the date and the runner stay text.

    A file with this header and the line 2026-11-02,Priya,3.1,29 gives
    [{"date": "2026-11-02", "runner": "Priya", "miles": 3.1, "minutes": 29}]
    A file with only the header gives [].
    """
    raise NotImplementedError("Not built yet.")


def miles_by_runner(runs):
    """Return a dictionary of each runner's total miles, from a list of runs.

    runs is a list like the one read_runs returns. The keys are the runners'
    names, in the order each one first appears, and each total is rounded to
    1 decimal place.

    Runs of Priya 3.1, Marcus 4.0 and Priya 2.5 give {"Priya": 5.6, "Marcus": 4.0}
    An empty list gives {}.
    """
    raise NotImplementedError("Not built yet.")


def write_summary(path, totals):
    """Write the totals to a new CSV file at path, with csv.DictWriter.

    totals is a dictionary like the one miles_by_runner returns. The file's
    header is runner,miles, then one line for each runner, in the
    dictionary's order. A file already at path is replaced.

    {"Priya": 5.6, "Marcus": 4.0} gives a file with these lines:
    runner,miles
    Priya,5.6
    Marcus,4.0
    """
    raise NotImplementedError("Not built yet.")


def save_goals(path, goals):
    """Save the goals dictionary to the JSON file at path, with indent=2.

    goals is a dictionary of each member's weekly goal in miles, such as
    {"Priya": 12, "Marcus": 10}. A file already at path is replaced.
    """
    raise NotImplementedError("Not built yet.")


def load_goals(path):
    """Return the goals dictionary saved in the JSON file at path.

    A file holding {"Priya": 12, "Marcus": 10} gives {"Priya": 12, "Marcus": 10}.
    When there's no file at path yet, return an empty dictionary, {}, instead
    of stopping with a FileNotFoundError.
    """
    raise NotImplementedError("Not built yet.")
