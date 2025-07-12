from issuecommand import issue_command

if __name__ == "__main__":
    issue_command("git add .", verbose=True)
    issue_command("git commit -m Your commit message", verbose=True)
    issue_command("git push  --force", verbose=True)
