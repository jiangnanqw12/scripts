#!/bin/bash

# Variables
ORIGINAL_REPO_PATH="/path/to/original-repo"
SUBMODULE_PATH="path/to/submodule"
NEW_REPO_PATH="/path/to/new-repo"

# Clone the original repository
git clone "$ORIGINAL_REPO_PATH" original-repo
cd original-repo || exit

# Filter the submodule
git filter-repo --path "$SUBMODULE_PATH" --path-rename "$SUBMODULE_PATH:/"

# Create the new repository
mkdir -p "$NEW_REPO_PATH"
cd "$NEW_REPO_PATH" || exit
git init

# Push the filtered content to the new repository
cd ../original-repo || exit
git remote add new-origin "$NEW_REPO_PATH"
git push new-origin master