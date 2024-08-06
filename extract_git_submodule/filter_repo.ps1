# Variables
$originalRepoPath = "git@github.com:jiangnanqw12/test-code.git"
$submodulePath = "automate_online-materials"
$newRepoPath = "git@github.com:jiangnanqw12/automate_online-materials.git"

# Clone the original repository
#git clone $originalRepoPath original-repo
Set-Location -Path "original-repo"

# Filter the submodule
git filter-repo --path "${submodulePath}/" --path-rename "${submodulePath}:"

# Create the new repository directory (locally)
Set-Location -Path ".."
git clone $newRepoPath new-repo
Set-Location -Path "new-repo"
git init

# Add filtered content to the new repository
Set-Location -Path "..\original-repo"
git remote add new-origin $newRepoPath
git push new-origin master

# Go back to the root directory
Set-Location -Path ".."