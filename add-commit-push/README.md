
# Add-Commit-Push Script

This Python script automates the common Git workflow:
`git add -A`, `git commit -m "message"`, and `git push`.

---

## Features

- Executes from the command line using:
  ```
  python add-commit-push.py
  ```

- Accepts a custom commit message:
  ```
  python add-commit-push.py -m "Your commit message"
  ```

- Optional force flag to skip confirmation:
  ```
  python add-commit-push.py -f
  ```

## Credit

ChatGPT is used for the command-line argument parsing section and
Eric Pouge In-Class Demo

