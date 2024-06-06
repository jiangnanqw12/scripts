# Variables
$originalRepoPath = "git@github.com:jiangnanqw12/test-code.git"
$submodulePath = "automate_online-materials"
$newRepoPath = "git@github.com:jiangnanqw12/automate_online-materials.git"

# Clone the original repository
git clone $originalRepoPath original-repo
Set-Location original-repo

# Filter the submodule
git filter-repo --path $submodulePath --path-rename "$submodulePath:/"

# Create the new repository
New-Item -ItemType Directory -Force -Path $newRepoPath
Set-Location $newRepoPath
git init

# Push the filtered content to the new repository
Set-Location ../original-repo
git remote add new-origin $newRepoPath
git push new-origin master