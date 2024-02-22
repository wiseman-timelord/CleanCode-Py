# Script: cleaner.ps1

# Clean dirty scripts
function CleanScriptFiles {
    Clear-Host
    PrintProgramTitle
    try {
        Write-Host "Backing Up Scripts.."
        BackupFiles 'Script'
        Write-Host "..Scripts Backed Up.`n"
        $scriptFiles = Get-ChildItem ".\Dirty" -File | Where-Object { DetermineScriptType $_.Name -ne 'Unknown' }
        if ($scriptFiles.Count -eq 0) {
            Write-Host "No Scripts In .\Dirty"
            return
        }
        Write-Host "Cleaning Scripts...`n"
        foreach ($file in $scriptFiles) {
            $global:FilePathName_c2l = $file.FullName
            $scriptType = DetermineScriptType $file.Name
            if ($scriptType -eq 'Unknown') {
                Write-Host "Bypassing Log: $($file.Name)`n"
                continue
            }
            Write-Host "Processing: $($file.Name)"

            $preStats = Get-FileStats
            Write-Host "State: Blanks=$($preStats.Blanks), Comments=$($preStats.Comments), Lines=$($preStats.Total)"
			
            # Assuming ProcessFile function modifies the file in-place
            $cleanContent = ProcessFile

            $postStats = Get-FileStats
            $reduction = CalculateReduction -PreTotal $preStats.Total -PostTotal $postStats.Total
            Write-Host "After: Blanks=$($postStats.Blanks), Comments=$($postStats.Comments), Lines=$($postStats.Total)"
            Write-Host "Total Reduction=$reduction%`n"

            # Move the cleaned file to ".\Clean" directory
            $cleanDestination = Join-Path ".\Clean" $file.Name
            Move-Item $file.FullName -Destination $cleanDestination -Force
            
            Start-Sleep -Seconds 1
        }
        Write-Host "...Scripts Cleaned."      
    } catch {
        Write-Host "Error Cleaning: $_"
    } finally {
		Write-Host ""
		PrintProgramSeparator
		Write-Host "Returning To Menu...`n"
        Start-Sleep -Seconds 3
    }
}

# Clean log files
function CleanLogFiles {
    param (
        [string]$LogDirectory = ".\Dirty"
    )
    Clear-Host
    PrintProgramTitle
    try {
        Write-Host "Backing Up Logs.."
        BackupFiles 'Log'
        Write-Host "..Logs Backed Up.`n"
        Start-Sleep -Seconds 1
        $logFiles = Get-ChildItem -Path $LogDirectory -Filter "*.log"
        if ($logFiles.Count -eq 0) {
            Write-Host "No Logs In .\Dirty"
            return
        }
        Write-Host "Cleaning Logs..`n"
        foreach ($logFile in $logFiles) {
            Write-Host "Processing: $($logFile.Name)"
            $logPath = $logFile.FullName
            $content = Get-Content -Path $logPath -Raw
            # Replace escape sequences for colors and styles in logs
            $cleanedContent = $content -replace '\x1b\[\d*;?\d*;?\d*m', ''
            Set-Content -Path $logPath -Value $cleanedContent
            Write-Host "Cleaned: $($logFile.Name)`n"
            Start-Sleep -Seconds 1

            # Move the cleaned file to ".\Clean" directory
            $cleanDestination = Join-Path ".\Clean" $logFile.Name
            Move-Item $logPath -Destination $cleanDestination -Force
        }
        Write-Host "..Logs Cleaned."
    } catch {
        Write-Host "Error Cleaning: $_"
    } finally {
        Write-Host ""
		PrintProgramSeparator
        Write-Host "Returning To Menu...`n"
        Start-Sleep -Seconds 2
    }
}

# Sanitize based on type
function SanitizeContentBasedOnType {
    param (
        [string]$line
    )
    $scriptType = $global:ScriptType_x6s
    $commentSyntax = $global:CommentMap_k6s[$scriptType]

    if ($scriptType -eq 'Batch' && ($line.Trim().StartsWith("REM") -or $line.Trim().StartsWith("::"))) {
        return $null
    } elseif ($line.Trim().StartsWith($commentSyntax)) {
        return $null
    } else {
        return $line.Trim()
    }
}


# Comment check
function IsCommentLine {
    param (
        [string]$Line
    )
    $ScriptType = $global:ScriptType_x6s
    $commentSyntax = $global:CommentMap_k6s[$ScriptType]
    if ($ScriptType -eq 'Batch') {
        return $Line.Trim().StartsWith("REM") -or $Line.Trim().StartsWith("::")
    } else {
        return $Line.Trim().StartsWith($commentSyntax)
    }
}


# Process file content
function ProcessFile {
    $ScriptType = $global:ScriptType_x6s
    $FileName = [System.IO.Path]::GetFileName($global:FilePathName_c2l)
    $Content = Get-Content -Path $global:FilePathName_c2l | ForEach-Object { $_.Trim() }
    $ProcessedContent = @("$($global:CommentMap_k6s[$ScriptType]) Script: $FileName")
    $SectionRegexPatterns = @{}
    foreach ($Section in $global:SectionMap_d8f[$ScriptType].Keys) {
        $patterns = $global:SectionMap_d8f[$ScriptType][$Section] -join "|"
        $SectionRegexPatterns[$Section] = $patterns
    }
    $InsertedSections = @{}
    foreach ($Line in $Content) {
        if (-not $Line -or $Line.StartsWith($global:CommentMap_k6s[$ScriptType])) { continue }
        foreach ($Section in $SectionRegexPatterns.Keys) {
            if ($Line -match $SectionRegexPatterns[$Section] -and -not $InsertedSections.ContainsKey($Section)) {
                $CommentToAdd = "$($global:CommentMap_k6s[$ScriptType]) $Section".ToUpper()
                $ProcessedContent += "", $CommentToAdd
                $InsertedSections[$Section] = $true
            }
        }
        $ProcessedContent += $Line
    }
    $ProcessedContent | Set-Content -Path $global:FilePathName_c2l
}
