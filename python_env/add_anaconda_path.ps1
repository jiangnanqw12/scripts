# Set the primary and secondary Anaconda paths
$primaryCondaPath = "C:\Users\shade\anaconda3"
$secondaryCondaPath = "C:\ProgramData\anaconda3"

# Check if the primary Anaconda path exists
if (Test-Path $primaryCondaPath) {
    $condaPath = $primaryCondaPath
} elseif (Test-Path $secondaryCondaPath) {
    $condaPath = $secondaryCondaPath
} else {
    Write-Error "Neither Anaconda path exists: $primaryCondaPath or $secondaryCondaPath"
    exit
}

$condaScriptsPath = "$condaPath\Scripts"
$condaLibraryBinPath = "$condaPath\Library\bin"

# Check if sub-paths exist
if (-Not (Test-Path $condaScriptsPath)) {
    Write-Error "The Scripts path does not exist: $condaScriptsPath"
    exit
}

if (-Not (Test-Path $condaLibraryBinPath)) {
    Write-Error "The Library\bin path does not exist: $condaLibraryBinPath"
    exit
}

# Add Anaconda path to the environment variable
$env:PATH = "$condaPath;$condaScriptsPath;$condaLibraryBinPath;$env:PATH"
Write-Output "Anaconda paths have been added to the environment variable"

# Open a new PowerShell session to apply changes
#Start-Process powershell
powershell