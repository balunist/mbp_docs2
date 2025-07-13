from issuecommand import issue_command

if __name__ == "__main__":
    issue_command("sphinx-build -b pdf source build/pdf", verbose=True)
