from issuecommand import issue_command

if __name__ == "__main__":
    issue_command("sphinx-build -b clean build/html", verbose=True)
