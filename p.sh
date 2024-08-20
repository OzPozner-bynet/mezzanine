#!/bin/bash

# Function to check if git is clean
is_git_clean() {
    git status --porcelain | grep -q .
    return $?
}
# Function to add all files and commit with timestamp
commit_and_push() {
     timestamp=$(date +"%Y-%m-%d-%H-%M-%S")
     git add . -A
     git commit -m "Automatic commit: $timestamp"
     git push 
}
# Check if git is clean
if is_git_clean; then
   echo "Git repository is not clean. Please commit or stash changes before running this script."
#   exit 1
fi

# Add, commit, and push
commit_and_push
echo "All files added, committed with timestamp, and pushed to origin/main."
