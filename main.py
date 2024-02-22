# Script: main.py

# Imports
import os, shutil, sys, time, datetime
from scripts.display import show_main_menu, clear_screen, draw_title, set_default_colors
from scripts.utility import process_script, run_old_files_maintenance, run_remove_unsupported_files
from Color_Console import color

# Global Variables
terminal_width = shutil.get_terminal_size().columns

# Global Maps
COMMENT_MAP = {
    "Python": "#",
    "PowerShell": "#",
    "MQL5": "//",
    "Batch": "REM"
}
SECTION_MAP = {
    "Python": {
        "import": [r"^import\s+\w+", r"^from\s+\w+\s+import\s+\w+"],
        "variable": [r"^\w+\s*=\s*.+"],
        "dictionary": [r"^[a-zA-Z_]+ = \[", r"^[a-zA-Z_]+ = {"],
        "function": [r"^def\s+\w+\(.*\):"]
    },
    "PowerShell": {
        "import": [r"^Import-Module\s+\w+", r"^\.\s+\.\\[a-zA-Z0-9_\-]+\.ps1"],
        "variable": [r"^\$\w+", r"\$global:\w+"],
        "dictionary": [r"^\$global:(\w+)\s*=\s*@{"],
        "function": [r"^function\s+[a-zA-Z_][a-zA-Z0-9_]*", r"^function\s+[a-zA-Z_][a-zA-Z0-9_]*\s*{"]
    },
    "Batch": {
        "import": [r"^REM IMPORT \w+"],
        "variable": [r"^set "],
        "dictionary": [r"^REM MAP .+"],
        "function": [r"^:[a-zA-Z_][a-zA-Z0-9_]*", r"^if .*\(", r"^for .*\("]
    },
    "MQL5": {
        "import": [r"^#import\s+\w+"],
        "input": [r"^\s*input\s+\w+\s+\w+\s*="],
        "variable": [r"^\s*double\s+\w+\s*=", r"^\s*int\s+\w+\s*=", r"^\s*string\s+\w+\s*=", r"^\s*bool\s+\w+\s*="],
        "function": [r"^(void|int|double|string|bool)\s+\w+\(.*\)"],
    }
}
FILE_EXTENSION_TO_TYPE_MAP = {
    ".py": "Python",
    ".ps1": "PowerShell",
    ".mq5": "MQL5",
    ".bat": "Batch"
}
FOLDERS_WITH_CUTOFFS = {
    './Backup': datetime.datetime.now() - datetime.timedelta(days=180),
    './Clean': datetime.datetime.now() - datetime.timedelta(days=120),
    './Reject': datetime.datetime.now() - datetime.timedelta(days=60),
}

# Function finalize_program
def initialize_program():
    clear_screen()
    draw_title()
    print("Initializing Program...\n")
    time.sleep(1)
    set_default_colors()
    time.sleep(1)
    run_old_files_maintenance(FOLDERS_WITH_CUTOFFS)
    time.sleep(1)
    run_remove_unsupported_files()
    time.sleep(1)
    print("...Program Initialized.\n")
    time.sleep(2)

# Function finalize_program
def finalize_program():
    draw_title()
    print("Finalizing Program...\n")
    print("\n...Program Finalized.")
    exit()


# Entry Point
if __name__ == "__main__":
    initialize_program()
    show_main_menu()
    finalize_program()