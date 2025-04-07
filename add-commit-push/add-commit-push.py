import subprocess
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Add, commit, and push changes.")
parser.add_argument("-m", "--message", type=str, help="Commit message")
parser.add_argument("-f", "--force", action="store_true", help="Skip confirmation")
args = parser.parse_args()

print("Add-Commit-Push")
print("Executing \"git status\":")
print("")

# Run the git status command
resultGitStatus = subprocess.run(["git", "status"], capture_output=True, text=True)
print(resultGitStatus.stdout)

# Prepare commands
commit_msg = args.message if args.message else "Update files."
commands = [
    ["git", "add", "-A"],
    ["git", "commit", "-m", commit_msg],
    ["git", "push"]
]

# Show commands before running
print("The following commands will be executed:")
print("git add -A")
print(f"git commit -m \"{commit_msg}\"")
print("git push")

# Confirm unless forced
if not args.force:
    confirm = input("\nProceed? (y/n): ").strip().lower()
    if confirm != "y":
        print("Aborted by user.")
        exit()

# Executing git add
print("")
print("Executing \"git add -A\":")
print("")

# git add command
resultGitAdd = subprocess.run(["git", "add", "-A"], capture_output=True, text=True)
print(resultGitAdd.stdout)
print("STDERR:")
print(resultGitAdd.stderr)

# Executing git commit
print("Executing \"git commit -m '{}'\":" .format(commit_msg))
print("")

# git commit command
resultGitCommit = subprocess.run(["git", "commit", "-m", commit_msg], capture_output=True, text=True)
print(resultGitCommit.stdout)
print("STDERR:")
print(resultGitCommit.stderr)

# Executing git push
print("Executing \"git push\":")
print("")

# git push command
resultGitPush = subprocess.run(["git", "push"], capture_output=True, text=True)
print(resultGitPush.stdout)
print("STDERR:")
print(resultGitPush.stderr)
