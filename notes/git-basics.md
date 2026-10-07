# Git basics

## What Git is
Git saves the history of my work. Each saved version is a commit, with the date, the author and my message. I can go back to any version, like the save points in a video game.

## How I send files to GitHub
1. `git add .`: put all changed files in the package (staging)
2. `git commit -m "add: notes on ssh keys"`: save the package locally with a message that says what changed
3. `git push`: upload the commits to GitHub

Flow: my files -> `git add` -> `git commit` -> `git push` -> GitHub

## Useful checks
- `git status`: shows what changed and what is staged
- `git log --oneline`: shows the history, one line per commit
- `git remote -v`: shows the GitHub address linked to my repo (origin)

## My identity in Git
- `git config --global user.name` and `user.email` are the signature written on each commit.
- It is only a label. It is not a login. Permission to push comes from the SSH key.

## Git and GitHub
- Git is the tool on my computer.
- GitHub is the website that stores my repositories online.
- They are linked by a remote address called `origin`.