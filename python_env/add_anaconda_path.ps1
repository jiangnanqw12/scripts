# Set the Anaconda path (modify according to your actual installation path)
$condaPath = "C:\Users\shade\anaconda3"
$condaScriptsPath = "$condaPath\Scripts"
$condaLibraryBinPath = "$condaPath\Library\bin"

# Add Anaconda path to the environment variable
$env:PATH = "$condaPath;$condaScriptsPath;$condaLibraryBinPath;$env:PATH"

# Open a new PowerShell session
powershell