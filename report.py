# Prints the club's week with your five functions from club.py, and writes summary.csv. Ready to use.
# Run it with: python report.py (in this folder, so it finds runs.csv and goals.json)
from club import load_goals, miles_by_runner, read_runs, save_goals, write_summary

runs = read_runs("runs.csv")
totals = miles_by_runner(runs)
goals = load_goals("goals.json")

print("Riverbend Running Club: this week")
print(len(runs), "runs logged")
for runner, miles in totals.items():
    goal = goals.get(runner, 0)
    if miles >= goal:
        print(f"{runner}: {miles} of {goal} miles, goal met!")
    else:
        print(f"{runner}: {miles} of {goal} miles, {round(goal - miles, 1)} to go")

write_summary("summary.csv", totals)
print("Saved summary.csv")

save_goals("goals-backup.json", goals)
print("Goals in the backup:", len(load_goals("goals-backup.json")))
print("Goals in a file that isn't there yet:", load_goals("no-goals-yet.json"))
