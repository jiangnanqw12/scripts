import os
import subprocess

# Variables
ORIGINAL_REPO_PATH = "/path/to/original-repo"
SUBMODULE_PATH = "path/to/submodule"
NEW_REPO_PATH = "/path/to/new-repo"

def run_command(command):
    """Run a shell command"""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        raise Exception(f"Command failed: {command}\n{stderr.decode('utf-8')}")
    return stdout.decode('utf-8')

def main():
    # Clone the original repository
    run_command(f"git clone {ORIGINAL_REPO_PATH} original-repo")
    os.chdir("original-repo")

    # Filter the submodule
    run_command(f"git filter-repo --path {SUBMODULE_PATH} --path-rename {SUBMODULE_PATH}:/")

    # Create the new repository
    os.makedirs(NEW_REPO_PATH, exist_ok=True)
    os.chdir(NEW_REPO_PATH)
    run_command("git init")

    # Push the filtered content to the new repository
    os.chdir("../original-repo")
    run_command(f"git remote add new-origin {NEW_REPO_PATH}")
    run_command("git push new-origin master")

if __name__ == "__main__":
    main()