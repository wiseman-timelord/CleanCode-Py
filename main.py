# Imports
import os
import shutil
import sys
from colorama import init, Fore, Style
from scripts.display import show_main_menu, clear_screen
from scripts.cleaner import process_script

# Initialization
sys.stdout.write("\x1b]2;ScriptClean\x07")  # Set terminal title
sys.stdout.flush()
if os.name == 'nt':
    os.system('color 70')  # Dark grey background, white text for Windows
else:
    os.system('echo -e "\\e[100m\\e[97m"')  # Dark grey background, white text for Unix
init(autoreset=True)

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
        "import": [r"^import\s+\w+"],
        "variable": [r"^\s*input\s+(int|double|string|ENUM_TIMEFRAMES)\s+\w+\s*=", r"^\s*(int|double|string)\s+\w+\s*="],
        "dictionary": [r"^double\[\]\s+\w+;", r"^int\[\]\s+\w+;", r"string\[\]\s+\w+;"],
        "function": [r"^(int|double|string|void|long|bool)\s+[a-zA-Z_][a-zA-Z0-9_]*\("]
    },
}

FILE_EXTENSION_TO_TYPE_MAP = {
    ".py": "Python",
    ".ps1": "PowerShell",
    ".mq5": "MQL5",
    ".bat": "Batch"
}

# Entry Point
if __name__ == "__main__":
    show_main_menu()