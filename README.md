# CleanCode-Py

### Status
Release. The release version of this program is working almost as intended, however, the source version of the program is being converted and rebranded to CodeClean-Py. Most of it is done, next steps are...
- Test & as required update, cleaning and commenting, for scripts.
- Test & as required updated, identification/insertion of entry point comment.
- Clean Ansii Codes From Logs works, but check again after completing scripts.
- Update documentation on GitHub below.
- Use, completed code and improvements, to update powershell version.

### Description
CleanCode-Py is a utility designed for AI developers to, optimize scripts and clean ansi codes from error logs...
- For scripts it enhances readability and efficiency, it efficiently trims unnecessary comments and spaces, producing a streamlined script. This is especially useful for AI programmers whom may have scripts with multiple long comments in each function, the results of embedded AI notations/instructions, therein, removing these comments can introduce errors, especially for novice programmers.
- For logs, specifically only ones that feature Ansii codes, it removes the Ansii codes, producing a Error Log readable through for example Notepad.

### Features
- **Minimal Comments** - The Processed Scripts retains only essential comments and spaces, typically at the beginning of functions, classes, or sections.
- **Multi-Script Support** -  Supporting Python `.py`, PowerShell `.ps1`, Batch `.bat`, and MQL5 `.mql5` formats, as well as Logs `.log`.

### Output
- Main Menu - Lists detected scripts/logs, and provides options (Alpha)...
```
=========================( CleanCode-Py )=========================










                       1. Clean Scripts,
                            (6 Found)

                       2. Clean Logs.
                            (0 Found)











------------------------------------------------------------------
Select; Options = 1-2, Refresh = R, Exit = X:

```
- Script cleaning statistics (Alpha)...
```
=========================( CleanCode-Py )=========================

Checking File Types..
..Checking ./Dirty Folder..
..All scripts supported.

Backing Up Scripts..
Backed Up: 4 Script(s)
..Scripts Backed Up.

Processing Scripts...

Cleaning Script: display.ps1
Before: Blanks=29, Comments=7, Lines=193
After: Blanks=0, Comments=2, Lines=134
Reduction: 30.57%

Cleaning Script: main.ps1
Before: Blanks=8, Comments=7, Lines=46
After: Blanks=0, Comments=2, Lines=30
Reduction: 34.78%

Cleaning Script: setup.py
Before: Blanks=6, Comments=2, Lines=96
After: Blanks=0, Comments=3, Lines=67
Reduction: 30.21%

Cleaning Script: utility.ps1
Before: Blanks=26, Comments=6, Lines=202
After: Blanks=0, Comments=2, Lines=137
Reduction: 32.18%

...Scripts Cleaned.

------------------------------------------------------------------
Returning To Menu...

```

##

### Usage
1. Run `Setup-Install.Bat` to setup directories and install requirements.
1. Deposit the script/log files you wish to clean in the `.\Dirty` folder.
2. Double-click `CleanCode-Py.bat` for easy launching.
3. Check the options on the menu, Scripts/Logs=1-2, Refresh=R, Exit=X.
4. If you selected 1 or 2, then check the ".\Clean" folder after processing  (it will over-write!).
5. IF you need the original then check the ".\Backup" folder (it will over-write!).

### Requirements
- Windows - Batch Support and Scripting Host, Enabled.
- Python - Version compatability to be calculated.
- Libraries - Check the requirements.txt (installed via Setup-Install.Bat)

### Notes
- This Program is a somewhat complete remake of "ScriptClean", you may find the, latest and only remaining, version as the oldest release available. ScriptClean was my first proper program, hence CodeClean-Py is somewhat of a return to the source.

## DISCLAIMER
This software is subject to the terms in License.Txt, covering usage, distribution, and modifications. For full details on your rights and obligations, refer to License.Txt.
