from issuecommand import issue_command

if __name__ == "__main__":
    print("Generating HTML documentation...")
    issue_command("sphinx-build -b html source build/html", verbose=True)
    print(f"HTML documentation generated successfully. Size of 'build/html' directory .")