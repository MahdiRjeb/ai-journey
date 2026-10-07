# Git basics

## How I send files to GitHub
1. `git add .`: put all changed files in the package (staging)
2. `git commit -m "add: notes on ssh keys"`: save the package locally with a message that says what changed
3. `git push`: upload the commits to GitHub

Flow: my files -> `git add` -> `git commit` -> `git push` -> GitHub

Useful checks:
- `git status`: shows what changed and what is staged
- `git log --oneline`: shows the history, one line per commit

First push on a new branch: `git push -u origin main` (only once).