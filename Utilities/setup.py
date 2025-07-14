from issuecommand import issue_command

if __name__ == "__main__":
    issue_command("pip install sphinx", verbose=True)
    issue_command("pip install sphinx_rtd_theme", verbose=True)
    issue_command("pip install rst2pdf", verbose=True)
    issue_command("pip install sphinxcontrib-spelling", verbose=True)
