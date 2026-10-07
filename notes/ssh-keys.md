# SSH keys

## What they are
- **Public key (.pub):** the lock I give to GitHub or a server. It can only check my identity, not fake it. It is safe to share.
- **Private key (no .pub):** stays on my computer and proves it's me. My computer uses it automatically when I push. If someone gets it, they can pretend to be me, so I never share it, paste it, or commit it.

## How to tell them apart
- **Public key:** one short line, starts with `ssh-ed25519`, and the file ends with `.pub`.
- **Private key:** many lines, starts with `-----BEGIN OPENSSH PRIVATE KEY-----`, and the file has no `.pub`.

## How it works
1. I run `git push`.
2. GitHub sends a random challenge.
3. My computer signs it with the private key (the key itself is never sent).
4. GitHub checks the signature with my public key. If it matches, I'm in.

## Commands I used
- `ssh-keygen -t ed25519 -C "my_email"`: create the key pair
- `cat ~/.ssh/id_ed25519.pub`: show the public key to copy it
- `ssh -T git@github.com`: test the connection ("Hi MahdiRjeb!" means success)
- `git clone git@github.com:MahdiRjeb/ai-journey.git`: copy the repository to my PC

## Mistakes I made and the fixes
- I left `your-username` in the command, so GitHub said "Repository not found". Fix: use my real username, `MahdiRjeb`.
- I typed my email instead of `git@github.com`, so Git tried to connect to gmail.com. Fix: the start of the address never changes, only the part after the colon is mine.
- I tried to clone before creating the repository. Fix: create it on github.com first, then clone it.
- My commit showed "0 insertions" because PowerShell's `>` saves in a format Git sees as binary. Fix: write files in VS Code.

## What I learned
- Each error message names its own cause, so I read it word by word.
- The private key never leaves my computer. Only the public key goes to GitHub.
- Git is the tool on my computer; GitHub is the website that stores my repositories.

