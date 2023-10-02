# Script: washup.py

# COMMENT_MAP
COMMENT_MAP = {
    "Python": "#",
    "PowerShell": "#",
    "Batch": "REM",
    "MQL5": "//"
}

# SECTION_MAP
SECTION_MAP = {
    "Python": {
        "import": ["import ", "from "],
        "global-variables": [" = ", " = None", " = []", " = {}"],
        "dictionaries": [" = {", ": {"],
        "function": "def ",
        "class": "class ",
        "loop": ["for ", "while "],
        "conditional": ["if ", "elif ", "else:"],
        "exception": ["try:", "except ", "finally:"],
        "with-statement": "with "
    },
    "PowerShell": {
        "function": "function ",
        "cmdlet": ["Get-", "Set-", "New-", "Remove-", "Invoke-", "Start-", "Stop-"],
        "loop": ["for(", "foreach(", "while("],
        "conditional": ["if(", "elseif(", "else{"],
        "exception": ["try {", "catch ", "finally {"],
        "pipeline": "|",
        "paths": ". \"",
        "global-variables": "$global:",
        "other-variables": "$"
    },
    "Batch": {
        "echo": "echo ",
        "set-variable": "set ",
        "goto": "goto ",
        "label": ":",
        "loop": "for ",
        "conditional": ["if ", "else "],
        "call": "call ",
        "exit": "exit "
    },
    "MQL5": {
        "input": "input ",
        "int": "int ",
        "function": ["void ", "double ", "bool "],
        "include": "#include "
    }
}

# Function identify_script_type
def identify_script_type(lines):
    for script, identifiers in SECTION_MAP.items():
        for _, value in identifiers.items():
            if isinstance(value, list):
                if any(line.startswith(v) for v in value for line in lines):
                    return script
            else:
                if any(line.startswith(value) for line in lines):
                    return script
    for line in lines:
        for script, identifiers in SECTION_MAP.items():
            for _, value in identifiers.items():
                if isinstance(value, list):
                    if any(line.startswith(v) for v in value):
                        return script
                else:
                    if line.startswith(value):
                        return script
    return "Unknown"

# Function to clean contents
def clean_file_content(lines, script_name, file_extension):
    script_type = identify_script_type(lines)
    if script_type == "Unknown":
        print("Warning: Unknown script type. No changes made.")
        return lines, 0, 0, 0

    # Calculate initial stats
    initial_comments_count = sum(1 for line in lines if line.strip().startswith(COMMENT_MAP[script_type]))
    initial_blank_lines_count = sum(1 for line in lines if not line.strip())

    # Remove comments and blank lines
    cleaned_lines = [line for line in lines if not line.strip().startswith(COMMENT_MAP[script_type]) and line.strip()]

    # Add the standard comment at the beginning
    cleaned_lines = add_standard_comments(cleaned_lines, script_type, script_name, file_extension)

    # Calculate the differences
    comments_removed = initial_comments_count
    blank_lines_removed = initial_blank_lines_count
    lines_removed = len(lines) - len(cleaned_lines)

    return cleaned_lines, lines_removed, blank_lines_removed, comments_removed



def add_standard_comments(lines, script_type, script_name, file_extension):
    new_lines = []
    if not lines:
        return []
    comment_prefix = COMMENT_MAP.get(script_type, "//")
    new_lines.append(f"{comment_prefix} Script: {script_name}\n")

    # Add script name
    new_lines.extend(lines)
    
    # Call the specific function based on script type
    if script_type == "Python":
        new_lines = add_python_comments(new_lines)
    elif script_type == "PowerShell":
        new_lines = add_powershell_comments(new_lines)
    elif script_type == "Batch":
        new_lines = add_batch_comments(new_lines)
    elif script_type == "MQL5":
        new_lines = add_mql5_comments(new_lines)

    return new_lines


def add_python_comments(lines):
    # Add Python-specific comments here
    # ...
    return lines

def add_powershell_comments(lines):
    # Add PowerShell-specific comments here
    # ...
    return lines

def add_batch_comments(lines):
    # Add Batch-specific comments here
    # ...
    return lines

def add_mql5_comments(lines):
    # Add MQL5-specific comments here
    # ...
    return lines
