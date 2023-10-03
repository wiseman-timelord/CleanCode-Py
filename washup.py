# Script: washup.py

# Imports
import re
import os
import shutil


# Dictionary for colors
COLORS = {
    "RED": "\033[91m",
    "YELLOW": "\033[93m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RESET": "\033[0m"
}

# Dictionary
COMMENT_MAP = {
    "Python": "#",
    "PowerShell": "#",
    "MQL4": "//",
    "MQL5": "//",
    "Batch": "REM"
}

# Dictionary
SECTION_MAP = {
    "Python": {
        "import": [r"import\s+\w+", r"from\s+\w+\s+import\s+\w+"],
        "variable": [r"\w+\s*=\s*.+"],
        "dictionary": [r"[a-zA-Z_]+ = \[", r"[a-zA-Z_]+ = {"],
        "function": [r"def\s+\w+\(.*\):"]
    },
    "PowerShell": {
        "import": [r"Import-Module\s+\w+"],
        "variable": [r"\$\w+", r"\$global:\w+"],
        "dictionary": [r"@{.*}"],
        "function": [r"function\s+\w+\s*{"]
    },
    "Batch": {
        "import": [r"REM IMPORT \w+"],
        "variable": [r"set "],
        "dictionary": [r"REM MAP .+"],
        "function": [r":[a-zA-Z_][a-zA-Z0-9_]*"]
    },
    "MQL4": {
        "import": [r"#include\s+<\w+\.mqh>"],
        "variable": [r"int\s+\w+;", r"double\s+\w+;", r"string\s+\w+;"],
        "dictionary": [r"double\[\]\s+\w+;", r"int\[\]\s+\w+;", r"string\[\]\s+\w+;"],
        "function": [r"(int|double|string|void)\s+[a-zA-Z_][a-zA-Z0-9_]*\("]
    },
    "MQL5": {
        "import": [r"import\s+\w+"],
        "variable": [r"int\s+\w+;", r"double\s+\w+;", r"string\s+\w+;"],
        "dictionary": [r"double\[\]\s+\w+;", r"int\[\]\s+\w+;", r"string\[\]\s+\w+;"],
        "function": [r"(int|double|string|void)\s+[a-zA-Z_][a-zA-Z0-9_]*\("]
    },
}



# Dictionary
FILE_EXTENSION_TO_TYPE_MAP = {
    ".py": "Python",
    ".ps1": "PowerShell",
    ".mql5": "MQL5",
    ".mql4": "MQL4",
    ".bat": "Batch"
}

# Function
def display_colored_text(text, color):
    print(f"{COLORS[color]}{text}{COLORS['RESET']}")

# Function
def determine_type(filename):
    file_extension = os.path.splitext(filename)[1].lower()
    script_type = FILE_EXTENSION_TO_TYPE_MAP.get(file_extension, "Unknown")
    if script_type == "Unknown":
        shutil.copy(f"./Scripts/{filename}", f"./Backup/{filename}")
        print(f"Unknown script type for '{filename}'. File has been backed up.")
    return script_type

# Function
def dict_to_regex(d):
    regex_patterns = {}
    for key, value in d.items():
        new_value = {}
        for sub_key, sub_value in value.items():
            if isinstance(sub_value, list):
                new_value[sub_key] = "|".join(sub_value)
            else:
                new_value[sub_key] = sub_value
        regex_patterns[key] = new_value
    return regex_patterns

# Function
def sanitize_script_content(lines, script_name, file_extension):
    script_type = determine_type(script_name)
    if script_type == "Unknown":
        print(" Warning: Unknown script type. No changes made.")
        return lines, 0, 0, 0, 0
    
    display_colored_text(f" Script type is '{script_type}' with extension '{file_extension}'.", "YELLOW")
    
    initial_comments_count = sum(1 for line in lines if line.strip().startswith(COMMENT_MAP[script_type]))
    initial_blank_lines_count = sum(1 for line in lines if not line.strip())
    comment_symbol = COMMENT_MAP[script_type]
    cleaned_lines = []
    for line in lines:
        if comment_symbol in line:
            line = line.split(comment_symbol, 1)[0].rstrip()
        if line.strip(): 
            cleaned_lines.append(line)
    cleaned_lines_before = len(cleaned_lines)
    cleaned_lines = insert_comments(cleaned_lines, script_type, script_name, file_extension)
    standard_comments_added = len(cleaned_lines) - cleaned_lines_before
    comments_removed = initial_comments_count - sum(1 for line in cleaned_lines if line.strip().startswith(comment_symbol))
    blank_lines_removed = initial_blank_lines_count - sum(1 for line in cleaned_lines if not line.strip())
    lines_removed = len(lines) - len(cleaned_lines)

    return (cleaned_lines, lines_removed, blank_lines_removed, comments_removed, standard_comments_added)

# Function
def insert_comments(lines, script_type, script_name, file_extension):
    new_lines = []
    if not lines:
        return []
    
    comment_prefix = COMMENT_MAP.get(script_type)
    if not comment_prefix:
        raise ValueError(f"Unsupported script type: {script_type}")

    new_lines.append(f"{comment_prefix} Script: {script_name}\n")
    
    sections_added = {
        "import": False,
        "variable": False,
        "dictionary": False,
        "function": False
    }
    
    for line in lines:
        stripped_line = line.strip()
        for section, patterns in SECTION_MAP[script_type].items():
            for pattern in patterns:
                try:
                    if re.search(str(pattern), stripped_line) and not sections_added[section]:
                        new_lines.append(f"\n{comment_prefix} {section.capitalize()}\n")
                        sections_added[section] = True
                        break
                except re.error as re_err:
                    continue
        new_lines.append(line)
    
    return new_lines


