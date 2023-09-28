# ScriptClean
Status: Working.

### Updated - 2023/09/28
- ScriptClean now supports, Python, Batch, Powershell and Mql5, and identifies some amount of syntax for each.
- Enhancements include color-coded console output, with distinct colors for regular text, lines, and errors.
- Improved the script through, optimizations, misc upgrades, implementation of maps and refracturing to 2 scripts.
- Screen width is now OS aware compatible with, linux and windows, shells.

### Description
ScriptClean is a Python utility designed to clean Python `.py`, PowerShell `.ps1`, Batch `.bat`, MetaTrader5 `.mt5`, and other script types. It removes unnecessary comments and blank lines to make your scripts more readable and efficient. The tool provides a user-friendly interface, complete with, color text and ASCII art, to guide you through the cleaning process. While it retains a comment and blank line at the start of functions or classes, those will be the only comments and blank lines you'll see :sunglasses:. In essence, cleaning files for a more concise context can be tedious and prone to errors. ScriptClean offers a reliable, safe, and logical method, saving you time and hassle.

### Features
1. **Identification of Script**: Uses simple rules to determine the type of script.
2. **Directory Management**: Automatically creates essential directories ("Scripts", "Backup", "Cleaned") if they don't exist.
3. **File Scanning**: Scans the "./Scripts" folder for `.py`, `.ps1`, and other script files.
4. **User Interface**: Presents a numbered list of discovered script files for easy selection.
5. **File Backup**: Backs up the chosen file to the "./Backup" folder before cleaning.
6. **File Cleaning**: Removes specific types of comments and blank lines based on user-defined rules.
7. **Essential Comments**: For Python scripts, it ensures there's a comment before all functions and classes.
8. **File Saving**: Stores the cleaned file in the "./Cleaned" folder.
9. **Original File Removal**: Deletes the original file from the "./Scripts" folder post-cleaning.
10. **Statistics Display**: Provides insights about the cleaning process, including the number of lines and comments removed.
11. **Looping Interface**: Facilitates continuous cleaning operations with options to clean another file or exit.

### Output
The Main Menu, and processing scripts...
```
============================================================================
  _________            .__        __   _________ .__
 /   _____/ ___________|__|______/  |_ \_   ___ \|  |   ____ _____    ____
 \_____  \_/ ___\_  __ \  \____ \   __\/    \  \/|  | _/ __ \\__  \  /    \
 /        \  \___|  | \/  |  |_> >  |  \     \___|  |_\  ___/ / __ \|   |  \
/_______  /\___  >__|  |__|   __/|__|   \______  /____/\___  >____  /___|  /
        \/     \/         |__|                 \/          \/     \/     \/
============================================================================
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Script Operations
----------------------------------------------------------------------------
 Scanning Folder...
 ...Scripts Found.
                             1. interface.py
                             2. model.py
                             3. utility.py
                             0. Clean All Sripts

 Select a file to clean (or 'quit' to exit): 0

 Cleaning Script 'interface.py'...
 Removed: 0 Lines, 10 Blanks, 2 Comments
 Difference: 150 > 140 - 6.67%

 Cleaning Script 'model.py'...
 Removed: 14 Lines, 24 Blanks, 7 Comments
 Difference: 155 > 117 - 24.52%

 Cleaning Script 'utility.py'...
 Removed: 0 Lines, 0 Blanks, 0 Comments
 Difference: 105 > 105 - 0.00%

```
...until no more files left...
```
=============================================================================
   _________            .__        __   _________ .__
  /   _____/ ___________|__|______/  |_ \_   ___ \|  |   ____ _____    ____
  \_____  \_/ ___\_  __ \  \____ \   __\/    \  \/|  | _/ __ \\__  \  /    \
  /        \  \___|  | \/  |  |_> >  |  \     \___|  |_\  ___/ / __ \|   |  \
 /_______  /\___  >__|  |__|   __/|__|   \______  /____/\___  >____  /___|  /
         \/     \/         |__|                 \/          \/     \/     \/
==============================================================================
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 Script Operations
------------------------------------------------------------------------------

 Scanning Folder...
 No Scripts Found!

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Program exited, press any key to continue...











```

### Usage - Windows
1. Deposit the script files you wish to clean in the `./Scripts` folder.
2. Double-click `ScriptClean.bat` for easy launching.
3. Adhere to the on-screen prompts to select a file for cleaning.
4. Check folder ".\Cleaned" after processes complete, backups are in ".\Backup".

### Usage - Linux (Untested)
1. Deposit the script files you wish to clean in the `./Scripts` folder.
2. Run `python main.py`, this may additionally require admin mode.
3. Adhere to the on-screen prompts to select a file for cleaning.
4. Check folder "./Cleaned" after processes complete, backups are in ".\Backup".

### Requirements
- Python 3.x
- Windows or Linux (untested), Operating System

### Notes
-Batch is somewhat more untested, but all formats require further, testing and refining.
-Improvement of display needed, processing of scripts needs to be in its own separated text section.

### Disclaimer
* While this program takes the error out of processing scripts, it also introduces the issue of moving scripts around, so remember to always exercise some level of caution with organizing the movements of your Master scripts.
* If you use of "#" a bit along the line in some abnormal method, it will also remove this, but, "###" and "##", such as for example "### USER:", are, tested and safe. This was the only rule update required during testing on the the 4 scripts for "Llama2Robot" at the time. 
* This tool is provided "as is" without any warranties. Always test the script on sample files before using it on important data. The authors are not responsible for any loss of data or functionality.
* The scripts produce, "Backup" and "Cleaned", versions of the scripts, if it broke your script, then use the backup for that one, and if there are no Backups, thats because you, moved or deleted, them.
