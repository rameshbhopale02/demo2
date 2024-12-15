#!/bin/bash

# Array of months
months=("April" "May" "June" "July" "August")

# Start and end year for commits
year=2024

# Loop through each month and create 10 commits
for month in "${months[@]}"; do
  for i in {1..10}; do
    # Generate a random day between 1 and 28 for the given month
    day=$(( (RANDOM % 28) + 1 ))
    
    # Create the commit date in the format YYYY-MM-DD
    commit_date="$year-$(date -d "$month 1, $year" +%m)-$day"
    
    # Set the commit date
    GIT_COMMITTER_DATE="$commit_date 12:00:00" git commit --allow-empty -m "Commit on $commit_date"
    
    # Optionally, you can make an actual change to a file (uncomment the following lines)
    # echo "Changes for $commit_date" >> file.txt
    # git add file.txt
  done
done
