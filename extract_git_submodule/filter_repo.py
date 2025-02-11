import os
import subprocess

# Variables
ORIGINAL_REPO_PATH = "git@github.com:jiangnanqw12/test-code.git"
SUBMODULE_PATH = r"005_video_process/yt-dlp"
NEW_REPO_PATH = "git@github.com:jiangnanqw12/video_download_scripts.git"
DEBUG_MODE=1

def run_command(command):
    """Run a shell command"""

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    
    if process.returncode != 0:
        raise Exception(f"Command failed: {command}\n{stderr.decode('utf-8')}")
    if DEBUG_MODE:
        print(stdout.decode())
        print(stderr.decode())
    return stdout.decode('utf-8')


def main():
    # Clone the original repository
    try:
        run_command(f"git clone {ORIGINAL_REPO_PATH} original-repo")
    except:
        pass
    
    os.chdir("original-repo")
    #git filter-repo --subdirectory-filter automate_online-materials
    # Filter the submodule
    # run_command(f"git filter-repo --path ${SUBMODULE_PATH}/ --path-rename ${SUBMODULE_PATH}:")
    # run_command(f"git filter-repo --subdirectory-filter {SUBMODULE_PATH}")
    run_command(f"git filter-repo --path \"{SUBMODULE_PATH}\" --force")
    # os.chdir("..")
    # # Create the new repository
    # os.makedirs(NEW_REPO_PATH, exist_ok=True)
    # os.chdir(NEW_REPO_PATH)
    # run_command("git init")

    # # Push the filtered content to the new repository
    # os.chdir("../original-repo")
    run_command(f"git remote add new-origin {NEW_REPO_PATH}")
    run_command("git push new-origin master")

if __name__ == "__main__":
    main()