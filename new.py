import os
import random
from datetime import datetime, timedelta

# Repository path (update this to your local repository's path)
REPO_PATH = "D:\SEMVII\Resume Project\emp\new"

# Set the range of months (April to August)
MONTHS = [4, 5, 6, 7, 8]
YEAR = 2024
COMMITS_PER_MONTH = 10

# Change directory to the repository
os.chdir(REPO_PATH)

def generate_random_datetime(month, year):
    """Generate a random datetime within the given month and year."""
    start_date = datetime(year, month, 1)
    if month == 12:
        end_date = datetime(year + 1, 1, 1) - timedelta(seconds=1)
    else:
        end_date = datetime(year, month + 1, 1) - timedelta(seconds=1)

    random_date = start_date + timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds()))
    )
    return random_date

def create_commit(commit_date):
    """Create a commit with the given date."""
    formatted_date = commit_date.strftime("%Y-%m-%dT%H:%M:%S")
    os.system(f'git add .')
    os.system(f'GIT_AUTHOR_DATE="{formatted_date}" GIT_COMMITTER_DATE="{formatted_date}" git commit -m "Random commit on {formatted_date}"')

# Generate and create commits
for month in MONTHS:
    for _ in range(COMMITS_PER_MONTH):
        random_date = generate_random_datetime(month, YEAR)
        with open("random_file.txt", "a") as f:
            f.write(f"Random commit at {random_date}\n")  # Modify a file to make a commit
        create_commit(random_date)

print("Random commits created for April to August.")
