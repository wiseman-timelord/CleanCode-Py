# ScriptClean

### Status: Under development (ensure to download release versions).
** Planned Work ** - There are still issues, works for reduction, doesnt work for complete re-integration of basic comments. will revisit later... 
- Maps and Code, for adding comments requires, tuning and bugfixing, since moving to RegEx.
- Stats for cleaning scripts still buggy, requires update of logic.
** Work Done ** - Things done for next release
- Expand compatibility to incorporate, batch and mql4 and mql5.
- Implementation of RegEx (better handling of processes).
- Improvements to interface ('r'=Re-Detect, 'd'=Debug, 'q'=Exit).

### Description
ScriptClean is a Python utility designed to clean Python `.py`, PowerShell `.ps1`. It removes unnecessary comments and blank lines to make your scripts more readable and efficient. The tool provides a user-friendly interface, complete with color text and ASCII art, to guide you through the cleaning process. While it retains a comment and blank line at the start of functions or classes, those will be the only comments and blank lines you'll see :sunglasses:. Cleaning files for a more concise context can be tedious and prone to errors. ScriptClean offers a reliable, safe, and logical method, saving you time and hassle. It's recommended to review both the original and cleaned outputs the first time you run the program to understand the differences the filter produces.

### Features
1. **Identification of Script**: Uses simple rules to determine the type of script.
2. **Directory Management**: Automatically creates essential directories ("Scripts", "Backup", "Cleaned") if they don't exist.
3. **File Scanning**: Scans the "./Scripts" folder for `.Py`, `.Ps1`, script files.
4. **User Interface**: Presents a numbered list of discovered script files for easy selection.
5. **File Backup**: Backs up the chosen file to the "./Backup" folder before cleaning.
6. **File Cleaning**: Removes specific types of comments and blank lines based on user-defined rules.
7. **Essential Comments**: For Python scripts, it ensures there's a comment before all functions and classes.
8. **File Saving**: Stores the cleaned file in the "./Cleaned" folder.
9. **Original File Removal**: Deletes the original file from the "./Scripts" folder post-cleaning.
10. **Statistics Display**: Provides insights about the cleaning process, including the number of lines and comments removed.
11. **Looping Interface**: Facilitates cleaning operations with options to, re-detect new files and clean again, or exit.

### Output
**Display Options**: Lists detected scripts and offers an option to "Clean All Scripts".
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
                             1. interface.py
                             2. message.py
                             3. model.py
                             4. utility.py
                             0. Clean All Sripts

 Select an option (or 'q' to exit):





```
**Feedback**: During cleaning, displays statistics, this is being improved.
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
 Script Operations:
------------------------------------------------------------------------------

 Identified Python script: 'interface.py'...
     Removed: 7 Blanks, 17 Comments,
     Added: -32 Blanks, 5 Comments,
     Change: 175 > 143 = 18.29%.

 Identified Python script: 'message.py'...
     Removed: 1 Blanks, 7 Comments,
     Added: -19 Blanks, 4 Comments,
     Change: 78 > 59 = 24.36%.

 Identified Python script: 'model.py'...
     Removed: 4 Blanks, 12 Comments,
     Added: -17 Blanks, 4 Comments,
     Change: 145 > 128 = 11.72%.

```
**Loop**: After process, then re-displays the menu until the user exits.
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
                             0. Re-Detect Scripts

 Select an option (or 'q' to exit):










```
##

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
- **Python Version**: Ensure you have Python 3.4-3.12 installed. You can verify this by running `python --version` or `python3 --version` in your terminal or command prompt.
- **Operating System**: ScriptClean is designed to work on Windows and Linux. While it has been primarily tested on Windows, Linux users should be able to use it, though it remains largely untested on this platform. Mac OS users might also be able to run the script, but this hasn't been verified.
- **Dependencies**: No external Python libraries are required. The script utilizes standard libraries like `os`, `shutil`, and `time`.

### Disclaimer
* While this program takes the error out of processing scripts, it also introduces the issue of moving scripts around, so remember to always exercise some level of caution with organizing the movements of your Master scripts.
* If you use of "#" a bit along the line in some abnormal method, it will also remove this, but, "###" and "##", such as for example "### USER:", are, tested and safe. This was the only rule update required during testing on the the 4 scripts for "Llama2Robot" at the time. 
* This tool is provided "as is" without any warranties. Always test the script on sample files before using it on important data. The authors are not responsible for any loss of data or functionality.
* The scripts produce, "Backup" and "Cleaned", versions of the scripts, if it broke your script, then use the backup for that one, and if there are no Backups, thats because you, moved or deleted, them.
