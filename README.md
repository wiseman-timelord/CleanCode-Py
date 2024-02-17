# CleanCode-Py

### Status: Working.
Working(ish). The batches for this program may only run on Windows 10 due to the different PowerShell launch commands required for various OS versions, that microsoft have bizarly chosen to use for each OS, and may cause endless launch loop on other systems.
- Plan for next update includes:
1) identification and processing of variables for `.Mq5` scripts.
2) identification of "while" as main loop in ".Ps1" scripts.
3) Clean Ansii Codes From Ps Error Logs.

### Description
CleanCode-Py is a utility designed for AI developers to optimize scripts, enhancing readability and efficiency. Supporting Python .py, PowerShell .ps1, Batch .bat, and MQL5 .mql5 formats, it efficiently trims unnecessary comments and spaces, producing a streamlined script. Its user-friendly interface, highlighted with colored text and ASCII art, guarantees a smooth experience. The tool retains only essential comments and spaces, typically at the beginning of functions, classes, or sections. CleanCode-Py ensures precision, reducing errors and time consumption, from manually cleaning scripts. The tool prioritizes comments for Imports, Variables, Maps, and Functions. While tailored for AI developers, other programmers can also benefit from its capabilities for final script refinement. The scripts for CleanCode-Py have now been cleaned with, CleanCode-Py, so, if you want examples, then examine the scripts. 

### Features
1. **Script Identification**: Employs rules to ascertain the script type, supporting `.py`, `.ps1`, `.bat`, and `.mql5`.
2. **Directory Management**: Seamlessly sets up vital directories ("Scripts", "Backup", "Cleaned") if absent.
3. **File Scanning**: Probes the "./Scripts" directory for supported script files.
4. **Interactive UI**: Showcases a numbered list of detected scripts for effortless selection.
5. **File Backup**: Safeguards the selected file in the "./Backup" directory pre-cleaning.
6. **Script Streamlining**: Excises specific comments and blank lines based on refined rules.
7. **Preserving Essentials**: Ensures the presence of a comment before functions, classes, or vital sections.
8. **File Archiving**: Deposits the refined script in the "./Cleaned" directory.
9. **Original File Management**: Erases the initial script from the "./Scripts" directory after refinement.
10. **Insightful Statistics**: Offers a detailed breakdown of the cleaning process, highlighting the number of lines and comments modified.
11. **Looping Interface**: Enables continuous cleaning operations with options to re-detect, clean anew, or gracefully exit.
12. **Concise Comments**: Comment details for, imports, variables, maps, functions, not yet perfected for all formats.
13. **Color Text**: Through use of colorama library, the color text is safe for, windows and linux.

### Output
**Display Options**: Lists detected scripts, and provides options...
```
==============================================================================
   _________            .__        __   _________ .__
  /   _____/ ___________|__|______/  |_ \_   ___ \|  |   ____ _____    ____
  \_____  \_/ ___\_  __ \  \____ \   __\/    \  \/|  | _/ __ \\__  \  /    \
  /        \  \___|  | \/  |  |_> >  |  \     \___|  |_\  ___/ / __ \|   |  \
 /_______  /\___  >__|  |__|   __/|__|   \______  /____/\___  >____  /___|  /
         \/     \/         |__|                 \/          \/     \/     \/
==============================================================================
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 Script Choices:
------------------------------------------------------------------------------

 Scanning Folder...
 ...Scripts Found.
                             1. batch_test.bat
                             2. mql5_test.Mql5
                             3. powershell_test.ps1
                             4. python_test.py
                             0. Clean All Scripts

 Select, '0-9' = Choice, 'r' = Re-detect, 'd' = Debug, 'q' = Exit:







++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
```
**Feedback**: Script cleaning statistics (on already somewhat clean scripts)...
```
==============================================================================
                                 SCRIPT CLEAN
==============================================================================
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 Processing Scripts:
------------------------------------------------------------------------------

 Next script from './Scripts' is: 'batch_test.bat',
 Script type is 'Batch' with extension 'bat'.
     Removed: 11 Blanks, 14 Comments,
     Added: 2 Blanks, 13 Comments,
     Change: 191 > 188 = 2.09%.

 Next script from './Scripts' is: 'mql5_test.Mql5',
 Script type is 'MQL5' with extension 'Mql5'.
     Removed: 12 Blanks, 44 Comments,
     Added: 4 Blanks, 16 Comments,
     Change: 410 > 378 = 14.63%.

 Next script from './Scripts' is: 'powershell_test.ps1',
 Script type is 'PowerShell' with extension 'ps1'.
     Removed: 2 Blanks, 10 Comments,
     Added: 7 Blanks, 9 Comments,
     Change: 200 > 188 = 6.50%.

 Next script from './Scripts' is: 'python_test.py',
 Script type is 'Python' with extension 'py'.
     Removed: 2 Blanks, 17 Comments,
     Added: 8 Blanks, 10 Comments,
     Change: 175 > 156 = 14.86%.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
```
**Loop**: After process, then re-displays the menu until the user exits...
```
==============================================================================
   _________            .__        __   _________ .__
  /   _____/ ___________|__|______/  |_ \_   ___ \|  |   ____ _____    ____
  \_____  \_/ ___\_  __ \  \____ \   __\/    \  \/|  | _/ __ \\__  \  /    \
  /        \  \___|  | \/  |  |_> >  |  \     \___|  |_\  ___/ / __ \|   |  \
 /_______  /\___  >__|  |__|   __/|__|   \______  /____/\___  >____  /___|  /
         \/     \/         |__|                 \/          \/     \/     \/
==============================================================================
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 Script Choices:
------------------------------------------------------------------------------

 Scanning Folder...
 No Scripts Found!
                           No Scripts In './Scripts'

 Select, '0-9' = Choice, 'r' = Re-detect, 'd' = Debug, 'q' = Exit:










++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
```
##

### Usage - Windows
1. Deposit the script files you wish to clean in the `.\Scripts` folder.
2. Double-click `CleanCode-Py.bat` for easy launching.
3. Adhere to the on-screen prompts to select a file for cleaning.
4. Check folder ".\Cleaned" after processes complete, backups are in ".\Backup".

### Usage - Linux & wsl
1. Deposit the script files you wish to clean in the `./Scripts` folder.
2. Run `python main.py`, this may additionally require admin mode.
3. Adhere to the on-screen prompts to select a file for cleaning.
4. Check folder "./Cleaned" after processes complete, backups are in "./Backup".

### Requirements
- **Python Version**: Ensure you have Python 3.4-3.12, you can verify this by running `python --version` or `python3 --version` in your, terminal or command prompt.
- **Operating System**: CleanCode-Py is designed to work on Windows and Linux. While it has been primarily tested on Windows, Linux users should be able to use it, though it remains largely untested on this platform. Mac OS users might also be able to run the script, but this hasn't been verified.
- **Dependencies**: No external Python libraries are required. The script utilizes standard libraries like `os`, `shutil`, `re` and `time`.

### Notes
- The 'd' for debug option, will, copy back all the "./Backup" files to "./Scripts" and delete the "./Cleaned" files; its used for, testing and development, basically do not use it unless you are developing the code.

## DISCLAIMER
This software is subject to the terms in License.Txt, covering usage, distribution, and modifications. For full details on your rights and obligations, refer to License.Txt.
