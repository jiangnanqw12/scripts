# Set the Anaconda path (modify according to your actual installation path)
condaPath="C:\Users\shade\anaconda3"
condaScriptsPath="$condaPath/bin"
condaLibraryBinPath="$condaPath/lib"

# Add Anaconda path to the environment variable
export PATH="$condaPath:$condaScriptsPath:$condaLibraryBinPath:$PATH"

# Open a new Bash session
bash