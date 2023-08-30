# ScriptClean

## Status: Beta (testing).

## Description
ScriptClean is a Python utility designed to clean Python `.py` and PowerShell `.ps1` scripts. It removes unnecessary comments and blank lines to make your scripts more readable and efficient. The tool provides a user-friendly interface, complete with ASCII art, to guide you through the cleaning process. It leaves the,  comment and blank line, at the start of a function, but that will be the only, comments and blank lines, you will see :sunglasses:.

## Features
1. **ASCII Art Display**: Enhances the console output with visually appealing ASCII art.
2. **Directory Management**: Automatically creates the necessary directories ("Scripts", "Backup", "Cleaned") if they don't exist.
3. **File Scanning**: Scans the "./Scripts" folder for `.py` and `.ps1` files.
4. **User Interface**: Offers a numbered list of found script files for easy selection.
5. **File Backup**: Backs up the selected file to the "./Backup" folder before cleaning.
6. **File Cleaning**: Removes specific types of comments and blank lines based on user-defined rules.
7. **File Saving**: Saves the cleaned file to the "./Cleaned" folder.
8. **Original File Removal**: Deletes the original file from the "./Scripts" folder after cleaning.
9. **Statistics Display**: Shows statistics about the cleaning process, including the number of lines and comments removed.
10. **Looping Interface**: Allows continuous cleaning operations with options to clean another file or exit.

## Output
The Main Menu...
```
============================================================================
  _________            .__        __   _________ .__
 /   _____/ ___________|__|______/  |_ \_   ___ \|  |   ____ _____    ____
 \_____  \_/ ___\_  __ \  \____ \   __\/    \  \/|  | _/ __ \\__  \  /    \
 /        \  \___|  | \/  |  |_> >  |  \     \___|  |_\  ___/ / __ \|   |  \
/_______  /\___  >__|  |__|   __/|__|   \______  /____/\___  >____  /___|  /
        \/     \/         |__|                 \/          \/     \/     \/
============================================================================

 Scanning Folder...
 ...Scripts Found.
                             1. interface.py
                             2. model.py
                             3. utility.py
                             0. Clean All Sripts

 Select a file to clean (or 'quit' to exit):
```

Cleaning "Llama2Robot" scripts...
```
 Cleaning Script 'interface.py'...
 Removed: 0 Lines, 10 Blanks, 2 Comments
 Difference: 150 > 140 - 6.67%

 Cleaning Script 'main.py'...
 Removed: 18 Lines, 21 Blanks, 4 Comments
 Difference: 121 > 82 - 32.23%

 Cleaning Script 'model.py'...
 Removed: 14 Lines, 24 Blanks, 7 Comments
 Difference: 155 > 117 - 24.52%

 Cleaning Script 'utility.py'...
 Removed: 0 Lines, 0 Blanks, 0 Comments
 Difference: 105 > 105 - 0.00%
```

## Usage
1. Place the Python files you want to clean in the `./Scripts` folder.
2. Run `ScriptClean.bat` if you are on Windows for easy launching. Alternatively, you can run the Python script directly, and I advise admin mode.
3. Follow the on-screen instructions to select a file for cleaning.
4. Review the cleaning statistics and either choose another file to clean or exit the program.
*  Warning! If you have use of "#" a bit along the line, it will remove, but, "###" and "##", are ok. 

## Requirements
- Python 3.x
- Windows or Linux (untested), Operating System

## Notes
- The script automatically creates the necessary directories if they don't exist.
- Always back up important files before running any script that modifies them.

## Disclaimer
This tool is provided "as is" without any warranties. Always test the script on sample files before using it on important data. The authors are not responsible for any loss of data or functionality.
The scripts produce, "Backup" and "Cleaned", versions of the scripts, if it broke your script, then use the backup for that one, and if there are no Backups, thats because you, moved or deleted, them.
