# Tests for club.py. Run them with: pytest (in the exercise folder, with the virtual environment active).
# Each test calls one of your functions with the values in its name and checks what it returns or writes. A failing
# test says what it called, what it expected and what came back.
# Every file a test reads or writes is in tmp_path, an empty folder pytest makes for that test alone, so the tests never
# touch runs.csv, goals.json or any other file of yours.
# You don't need to change this file.
import csv
import json

from club import load_goals, miles_by_runner, read_runs, save_goals, write_summary

HEADER = "date,runner,miles,minutes\n"


def check(call, got, expected):
    """Fails with a message that says what the call returned and what it should return."""
    assert got == expected, f"{call} should return {expected!r}, but it returned {got!r}."


def check_file(what, got, expected):
    """Fails with a message that says what the file holds and what it should hold."""
    assert got == expected, f"{what} should hold {expected!r}, but it holds {got!r}."


def write_text(path, text):
    """Writes a test's own file, such as a small runs.csv, into its tmp_path folder."""
    with open(path, "w", newline="", encoding="utf-8") as file:
        file.write(text)


def test_1_read_runs_one_run_priya_3_1_miles_in_29_minutes(tmp_path):
    path = tmp_path / "runs.csv"
    write_text(path, HEADER + "2026-11-02,Priya,3.1,29\n")
    check("read_runs on a runs.csv holding 2026-11-02,Priya,3.1,29", read_runs(path),
          [{"date": "2026-11-02", "runner": "Priya", "miles": 3.1, "minutes": 29}])


def test_2_read_runs_three_runs_in_the_files_order(tmp_path):
    path = tmp_path / "runs.csv"
    write_text(path, HEADER + "2026-11-02,Priya,3.1,29\n2026-11-03,Marcus,4.0,38\n2026-11-04,Priya,2.5,24\n")
    check("read_runs on a runs.csv with runs by Priya, Marcus and Priya", read_runs(path), [
        {"date": "2026-11-02", "runner": "Priya", "miles": 3.1, "minutes": 29},
        {"date": "2026-11-03", "runner": "Marcus", "miles": 4.0, "minutes": 38},
        {"date": "2026-11-04", "runner": "Priya", "miles": 2.5, "minutes": 24},
    ])


def test_3_read_runs_keeps_the_e_with_two_dots_in_zoe(tmp_path):
    path = tmp_path / "runs.csv"
    write_text(path, HEADER + "2026-11-03,Zoë,5.2,47\n")
    check("read_runs on a runs.csv holding 2026-11-03,Zoë,5.2,47", read_runs(path),
          [{"date": "2026-11-03", "runner": "Zoë", "miles": 5.2, "minutes": 47}])


def test_4_read_runs_only_the_header_gives_an_empty_list(tmp_path):
    path = tmp_path / "runs.csv"
    write_text(path, HEADER)
    check("read_runs on a runs.csv holding only the header", read_runs(path), [])


def test_5_miles_by_runner_priya_3_1_and_2_5_marcus_4_0():
    runs = [
        {"date": "2026-11-02", "runner": "Priya", "miles": 3.1, "minutes": 29},
        {"date": "2026-11-03", "runner": "Marcus", "miles": 4.0, "minutes": 38},
        {"date": "2026-11-04", "runner": "Priya", "miles": 2.5, "minutes": 24},
    ]
    check("miles_by_runner on runs of Priya 3.1, Marcus 4.0 and Priya 2.5", miles_by_runner(runs), {"Priya": 5.6, "Marcus": 4.0})


def test_6_miles_by_runner_priya_3_1_2_5_and_4_4_rounds_to_10_0():
    runs = [
        {"date": "2026-11-02", "runner": "Priya", "miles": 3.1, "minutes": 29},
        {"date": "2026-11-04", "runner": "Priya", "miles": 2.5, "minutes": 24},
        {"date": "2026-11-08", "runner": "Priya", "miles": 4.4, "minutes": 41},
    ]
    check("miles_by_runner on runs of Priya 3.1, 2.5 and 4.4", miles_by_runner(runs), {"Priya": 10.0})


def test_7_miles_by_runner_no_runs_gives_an_empty_dictionary():
    check("miles_by_runner([])", miles_by_runner([]), {})


def test_8_write_summary_priya_5_6_and_marcus_4_0(tmp_path):
    path = tmp_path / "summary.csv"
    write_summary(path, {"Priya": 5.6, "Marcus": 4.0})
    with open(path, newline="", encoding="utf-8") as file:
        rows = list(csv.reader(file))
    check_file('summary.csv, after write_summary(path, {"Priya": 5.6, "Marcus": 4.0}),', rows,
               [["runner", "miles"], ["Priya", "5.6"], ["Marcus", "4.0"]])


def test_9_write_summary_no_runners_writes_only_the_header(tmp_path):
    path = tmp_path / "summary.csv"
    write_summary(path, {})
    with open(path, newline="", encoding="utf-8") as file:
        rows = list(csv.reader(file))
    check_file("summary.csv, after write_summary(path, {}),", rows, [["runner", "miles"]])


def test_10_write_summary_replaces_an_old_summary(tmp_path):
    path = tmp_path / "summary.csv"
    write_text(path, "runner,miles\nLuis,99.9\n")
    write_summary(path, {"Zoë": 8.2})
    with open(path, newline="", encoding="utf-8") as file:
        rows = list(csv.reader(file))
    check_file('summary.csv, after write_summary(path, {"Zoë": 8.2}) over an old one,', rows,
               [["runner", "miles"], ["Zoë", "8.2"]])


def test_11_save_goals_priya_12_and_marcus_10(tmp_path):
    path = tmp_path / "goals.json"
    save_goals(path, {"Priya": 12, "Marcus": 10})
    with open(path, encoding="utf-8") as file:
        saved = json.load(file)
    check_file('goals.json, after save_goals(path, {"Priya": 12, "Marcus": 10}),', saved, {"Priya": 12, "Marcus": 10})


def test_12_save_goals_lays_the_file_out_with_indent_2(tmp_path):
    path = tmp_path / "goals.json"
    save_goals(path, {"Priya": 12, "Marcus": 10})
    with open(path, encoding="utf-8") as file:
        text = file.read()
    check_file('goals.json, after save_goals(path, {"Priya": 12, "Marcus": 10}),', text,
               '{\n  "Priya": 12,\n  "Marcus": 10\n}')


def test_13_load_goals_reads_priya_12_and_zoe_15(tmp_path):
    path = tmp_path / "goals.json"
    write_text(path, '{"Priya": 12, "Zoë": 15}')
    check('load_goals on a goals.json holding {"Priya": 12, "Zoë": 15}', load_goals(path), {"Priya": 12, "Zoë": 15})


def test_14_load_goals_no_file_yet_gives_an_empty_dictionary(tmp_path):
    check("load_goals on a goals.json that isn't there", load_goals(tmp_path / "goals.json"), {})


def test_15_save_goals_then_load_goals_gives_the_same_goals(tmp_path):
    path = tmp_path / "goals.json"
    goals = {"Priya": 12, "Marcus": 10, "Zoë": 15, "Luis": 5}
    save_goals(path, goals)
    check("load_goals on the goals.json save_goals wrote", load_goals(path), goals)
