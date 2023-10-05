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
        "import": [r"Import-Module\s+\w+", r"\.\s+\.\\[a-zA-Z0-9_\-]+\.ps1"],
        "variable": [r"\$\w+", r"\$global:\w+"],
        "dictionary": [r"@{.*}"],
        "function": [r"function\s+[a-zA-Z_][a-zA-Z0-9_]*", r"function\s+[a-zA-Z_][a-zA-Z0-9_]*\s*{"]
    },
    "Batch": {
        "import": [r"REM IMPORT \w+"],
        "variable": [r"set "],
        "dictionary": [r"REM MAP .+"],
        "function": [r":[a-zA-Z_][a-zA-Z0-9_]*", r"^if .*\(", r"^for .*\("]
    },
    "MQL5": {
        "import": [r"import\s+\w+"],
        "variable": [r"^\s*input\s+(int|double|string|ENUM_TIMEFRAMES)\s+\w+\s*=", r"^\s*(int|double|string)\s+\w+\s*="],
        "dictionary": [r"double\[\]\s+\w+;", r"int\[\]\s+\w+;", r"string\[\]\s+\w+;"],
        "function": [r"(int|double|string|void)\s+[a-zA-Z_][a-zA-Z0-9_]*\("]
    },
}



# Dictionary
FILE_EXTENSION_TO_TYPE_MAP = {
    ".py": "Python",
    ".ps1": "PowerShell",
    ".mql5": "MQL5",
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
    comments_removed = abs(initial_comments_count - sum(1 for line in cleaned_lines if line.strip().startswith(comment_symbol)))
    blank_lines_removed = abs(initial_blank_lines_count - sum(1 for line in cleaned_lines if not line.strip()))
    lines_removed = abs(len(lines) - len(cleaned_lines))

    return (cleaned_lines, lines_removed, blank_lines_removed, comments_removed, standard_comments_added)

# Function
def format_name(name, script_type):
    """Format the name based on the given rules."""
    if script_type == "Python":
        words = [word for word in name.split("_")]
    elif script_type == "PowerShell":
        words = [word.capitalize() for word in name.split("-") if word[0].isupper()]  # Only consider words that start with an uppercase letter
    elif script_type == "MQL5":
        words = re.findall(r'[A-Z][a-z]*', name)  # Split based on capital letters
    else:
        words = [name]

    # If there's only one word, return that word
    if len(words) == 1:
        return words[0].capitalize()
    # If there are two or more words, use the first and last words
    else:
        return ' '.join([words[0].capitalize(), words[-1].capitalize()])

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

        # Debug: Print the current line being processed
        print(f"Processing line: {stripped_line}")

        # Skip lines that start with a space
        if line.startswith(' '):
            new_lines.append(line)
            continue

        formatted_name = ""  # Initialize to avoid UnboundLocalError

        for section, patterns in SECTION_MAP[script_type].items():
            for pattern in patterns:
                try:
                    match = re.search(str(pattern), stripped_line)
                    if match:
                        # Debug: Print the matched pattern and section
                        print(f"Matched pattern: {pattern} for section: {section}")

                        if section == "function":
                            if script_type == "Batch":
                                formatted_name = f"{comment_prefix} Function"
                                new_lines.append("\n" + formatted_name + "\n")
                                continue
                            elif script_type == "Python":
                                func_name_match = re.search(r"^def (\w+)", stripped_line)
                            elif script_type == "PowerShell":
                                func_name_match = re.search(r"^function ([\w-]+)", stripped_line)  # Adjusted regex here
                            else:
                                func_name_match = re.search(r"\b\w+(\s+\w+)?\(", stripped_line)
                            
                            if func_name_match:
                                func_name = func_name_match.group(1)
                                # Debug: Print the extracted function name
                                print(f"Extracted function name: {func_name}")
                                formatted_name = f"{comment_prefix} Function {format_name(func_name, script_type)}"
                                new_lines.append("\n" + formatted_name + "\n")
                        elif section == "dictionary":
                            dict_name = match.group().split("=")[0].strip().replace("$", "").replace("@", "")
                            formatted_name = f"{comment_prefix} Dictionary {format_name(dict_name, script_type)}"
                            new_lines.append("\n" + formatted_name + "\n")
                        elif section in ["import", "variable"] and not sections_added[section]:
                            new_lines.append(f"\n{comment_prefix} {section.capitalize()}s\n")
                            sections_added[section] = True
                        break
                except re.error as re_err:
                    continue
        new_lines.append(line)

    return new_lines