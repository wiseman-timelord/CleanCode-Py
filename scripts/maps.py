# Script: maps.py

# Imports
import datetime

# Map COMMENT_MAP
COMMENT_MAP = {
    "Python": "#",
    "PowerShell": "#",
    "MQL5": "//",
    "Batch": "REM"
}

# Map SECTION_MAP
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

# Map FILE_EXTENSION_TO_TYPE_MAP
FILE_EXTENSION_TO_TYPE_MAP = {
    ".py": "Python",
    ".ps1": "PowerShell",
    ".mq5": "MQL5",
    ".bat": "Batch"
}

# Map FOLDERS_WITH_CUTOFFS
FOLDERS_WITH_CUTOFFS = {
    './Backup': datetime.datetime.now() - datetime.timedelta(days=180),
    './Clean': datetime.datetime.now() - datetime.timedelta(days=120),
    './Reject': datetime.datetime.now() - datetime.timedelta(days=60),
}