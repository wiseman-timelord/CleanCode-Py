# Script: utility.ps1

# Backup before process
function BackupFiles {
    param (
        [string]$FileType
    )
	try {
        $files = $null
        switch ($FileType) {
            'Script' {
                $files = Get-ChildItem ".\Dirty" -File | Where-Object { $_.Extension -match '\.(ps1|py|bat|mq5)$' }
            }
            'Log' {
                $files = Get-ChildItem ".\Dirty" -File | Where-Object { $_.Extension -eq '.log' }
            }
        }
        foreach ($file in $files) {
            $destination = Join-Path ".\Backup" $file.Name
            [System.IO.File]::Copy($file.FullName, $destination, $true)
        }
		Write-Host "Backed Up: $($files.Count) $($FileType)s"
    } catch {
        Write-Host "Backup failed, $_"
    }
}


# Script type determination
function DetermineScriptType {
    param ([string]$filename)
    $scriptType = switch ([System.IO.Path]::GetExtension($filename).ToLower()) {
        '.py' { 'Python' }
        '.ps1' { 'PowerShell' }
        '.bat' { 'Batch' }
        '.mq5' { 'MQL5' }
        default { 'Unknown' }
    }
    $global:ScriptType_x6s = $scriptType
    return $scriptType
}

# Stats calculation
function Get-FileStats {
    $global:CurrentContent_o4s = Get-Content $global:FilePathName_c2l
    $stats = @{'Blanks' = 0; 'Comments' = 0; 'Total' = 0}
    foreach ($line in $global:CurrentContent_o4s) {
        $stats['Total']++
        if (-not $line.Trim()) {
            $stats['Blanks']++
            continue
        }
        if (IsCommentLine -Line $line) {
            $stats['Comments']++
        }
    }
    return $stats
}

# Reduction calculation
function CalculateReduction {
    param (
        [int]$PreTotal,
        [int]$PostTotal
    )
    return "{0:N2}" -f ((($PreTotal - $PostTotal) / $PreTotal) * 100)
}

# Old files maintenance
function Run-OldFilesMaintenance {
    $foldersWithCutoffs = @{
        '.\Backup' = (Get-Date).AddMonths(-6)
        '.\Clean' = (Get-Date).AddMonths(-4)
        '.\Reject' = (Get-Date).AddMonths(-2)
    }

    Write-Host "Checking Old files.."
    foreach ($folder in $foldersWithCutoffs.Keys) {
        $cutoffDate = $foldersWithCutoffs[$folder]
        $oldFiles = Get-ChildItem $folder -File | Where-Object { $_.LastWriteTime -lt $cutoffDate }

        if ($oldFiles.Count -gt 0) {
            Write-Host "Detected In: ${folder}"
            foreach ($file in $oldFiles) {
                Write-Host "Removing: $($file.Name)"
                Remove-Item $file.FullName -Force
            }
        } else {
            Write-Host "Checked: $folder"
        }
    }
    Write-Host "..Maintenance done.`n"
}

# Unsupported files handler
function Run-RemoveUnsupportedFiles {
    $allowedExtensions = @('.ps1', '.py', '.bat', '.mq5', '.log')
    $scriptFiles = Get-ChildItem ".\Dirty" -File
    $unsupportedFiles = $scriptFiles | Where-Object { $_.Extension.ToLower() -notin $allowedExtensions }
    Write-Host "Checking .\Dirty Folder.."
    if ($unsupportedFiles.Count -gt 0) {
        Write-Host "..Unsupported Scripts!"
        foreach ($file in $unsupportedFiles) {
            $destination = Join-Path ".\Reject" $file.Name
            Move-Item $file.FullName -Destination $destination -Force
            Write-Host "Rejected: $($file.Name)"
        }
    } else {
        Write-Host "..All scripts supported."
    }
	Write-Host ""
}
