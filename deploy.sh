#!/bin/sh

# If a command fails then the deploy stops
set -e

printf "\033[0;32mDeploying updates to GitHub...\033[0m\n"

# Build the project.
pelican content -o output
#pelican --listen

#cd output
#python3 -m http.server 8005

# Go To Outputfolder
cd output

# Add changes to git.
git add .

# Commit changes.
msg="rebuilding site $(date)"
if [ -n "$*" ]; then
	msg="$*"
fi
git commit -m "$msg"

# Push source and build repos.
git push origin master

#Move back to original project
cd ..

printf "\033[0;32mDone deploying to GitHub...\033[0m\n"