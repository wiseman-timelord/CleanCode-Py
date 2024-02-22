# main.ps1 - Initialization and Entry Point for CleanCode Program

# Import external scripts
. .\scripts\display.ps1
. .\scripts\utility.ps1
. .\scripts\cleaner.ps1

# Global variables
$global:FilePathName_c2l = ""
$global:ScriptType_x6s = ""
$global:CurrentContent_o4s = ""

# Global Dictionaries
$global:CommentMap_k6s = @{
    "Python" = "#"
    "PowerShell" = "#"
    "MQL5" = "//"
    "Batch" = "REM"
}
$global:SectionMap_d8f = @{
    "Python" = @{
        "import" = @('^import\s+\w+', '^from\s+\w+\s+import\s+\w+')
        "variable" = @('^\w+\s*=\s*.+')
        "dictionary" = @('^[a-zA-Z_]+ = \[', '^[a-zA-Z_]+ = {')
        "function" = @('^def\s+\w+\(.*\):')
    }
    "PowerShell" = @{
        "import" = @('^Import-Module\s+\w+', '^\.\s+\.\\[a-zA-Z0-9_\-]+\.ps1')
        "variable" = @('^\$\w+', '`$global:\w+')
        "dictionary" = @('`$global:(\w+)\s*=\s*@{')
        "function" = @('^function\s+[a-zA-Z_][a-zA-Z0-9_]*', '^function\s+[a-zA-Z_][a-zA-Z0-9_]*\s*{')
    }
    "Batch" = @{
        "import" = @('^REM IMPORT \w+')
        "variable" = @('^set ')
        "dictionary" = @('^REM MAP .+')
        "function" = @('^:[a-zA-Z_][a-zA-Z0-9_]*', '^if .*\(', '^for .*\(')
    }
    "MQL5" = @{
        "import" = @('^import\s+\w+')
        "variable" = @('^\s*input\s+(int|double|string|ENUM_TIMEFRAMES)\s+\w+\s*=', '^\s*(int|double|string)\s+\w+\s*=')
        "dictionary" = @('^double\[\]\s+\w+;', '^int\[\]\s+\w+;', 'string\[\]\s+\w+;')
        "function" = @('^(int|double|string|void|long|bool)\s+[a-zA-Z_][a-zA-Z0-9_]*\(')
    }
}

# Initialize program
function script-InitializationCode {
	Clear-Host
	PrintProgramTitle
	Start-Sleep -Seconds 1
	Set-ConfigureDisplay
	Start-Sleep -Seconds 1
    Run-OldFilesMaintenance
	Start-Sleep -Seconds 1
	Run-RemoveUnsupportedFiles
	Start-Sleep -Seconds 1
	Write-Host "Powershell Script Initialized...`n"
    Start-Sleep -Seconds 2
}

# Exit Program
function script-FinalizationCode {
    Clear-Host
	PrintProgramTitle
    Write-Host "`n....Powershell Script Exiting.`n"
    Start-Sleep -Seconds 2
	exit
}

# Main loop
function Main-Loop {
    Display-PrimaryMenu
}

# Entry point
script-InitializationCode
Main-Loop
script-FinalizationCode
