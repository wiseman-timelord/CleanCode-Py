# CleanCode-Py

### Status
Release. The release version of this program is working almost as intended, however, the source version of the program is being converted and rebranded to CodeClean-Py. NExt steps are...
- Test & as required update, cleaning and commenting, for scripts.
- Test & as required update, Clean Ansii Codes From Logs.
- Test & as required updated, identification/insertion of entry point comment.
- Update documentation on GitHub below.

### Description
CleanCode-Py is a utility designed for AI developers to optimize scripts, enhancing readability and efficiency. Supporting Python .py, PowerShell .ps1, Batch .bat, and MQL5 .mql5 formats, it efficiently trims unnecessary comments and spaces, producing a streamlined script. Its user-friendly interface, highlighted with colored text and ASCII art, guarantees a smooth experience. The tool retains only essential comments and spaces, typically at the beginning of functions, classes, or sections. CleanCode-Py ensures precision, reducing errors and time consumption, from manually cleaning scripts. The tool prioritizes comments for Imports, Variables, Maps, and Functions. While tailored for AI developers, other programmers can also benefit from its capabilities for final script refinement. The scripts for CleanCode-Py have now been cleaned with, CleanCode-Py, so, if you want examples, then examine the scripts. 

### Features
- To be detailed.

### Output
- Main Menu - Lists detected scripts/logs, and provides options...
```
=========================( CleanCode-Py )=========================










                       1. Clean Scripts,
                            (6 Found)

                       2. Clean Logs.
                            (0 Found)











------------------------------------------------------------------
Select; Options = 1-2, Refresh = R, Exit = X:

```
- Script cleaning statistics...
```
=========================( CleanCode-Py )=========================

Checking File Types..
Checking ./Dirty Folder..
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
