# Script: washup.py

import re

# COMMENT_MAP
COMMENT_MAP = {
    "Python": "#",
    "PowerShell": "#"
}

# SECTION_MAP
SECTION_MAP = {
    "Python": {
        "import": [r"import\s+\w+", r"from\s+\w+\s+import\s+\w+"],
        "variable": [r"^\w+\s*=\s*.+"],
        "map": [r"[a-zA-Z_]+ = \[", r"[a-zA-Z_]+ = \{"],
        "function": r"def\s+\w+\(.*\):"
    },
    "PowerShell": {
        "import": [r"Import-Module\s+\w+"],
        "variable": [r"\$\w+", r"\$global:\w+"],
        "map": [r"@{.*}"],
        "function": r"function\s+\w+\s*{"
    }
}

# Function identify_script_type
def identify_script_type(lines):
    for script, identifiers in SECTION_MAP.items():
        for _, value in identifiers.items():
            if isinstance(value, list):
                if any(re.match(v, line) for v in value for line in lines):
                    return script
            else:
                if any(re.match(value, line) for line in lines):
                    return script
    return "Unknown"

# Function to clean contents
def clean_file_content(lines, script_name, file_extension):
    script_type = identify_script_type(lines)
    if script_type == "Unknown":
        print("Warning: Unknown script type. No changes made.")
        return lines, 0, 0, 0, 0

    # Calculate initial stats
    initial_comments_count = sum(1 for line in lines if line.strip().startswith(COMMENT_MAP[script_type]))
    initial_blank_lines_count = sum(1 for line in lines if not line.strip())

    # Remove comments and blank lines
    comment_symbol = COMMENT_MAP[script_type]
    cleaned_lines = [line for line in lines if comment_symbol not in line and line.strip() != ""]

    # Add the standard comment at the beginning
    cleaned_lines_before = len(cleaned_lines)
    cleaned_lines = add_standard_comments(cleaned_lines, script_type, script_name, file_extension)
    standard_comments_added = len(cleaned_lines) - cleaned_lines_before

    # Calculate the differences
    comments_removed = initial_comments_count - sum(1 for line in cleaned_lines if line.strip().startswith(comment_symbol))
    blank_lines_removed = initial_blank_lines_count - sum(1 for line in cleaned_lines if not line.strip())
    lines_removed = len(lines) - len(cleaned_lines)

    return cleaned_lines, lines_removed, blank_lines_removed, comments_removed, standard_comments_added


# Function to add standard comments
def add_standard_comments(lines, script_type, script_name, file_extension):
    new_lines = []
    if not lines:
        return []
    comment_prefix = COMMENT_MAP.get(script_type, "//")
    new_lines.append(f"{comment_prefix} Script: {script_name}\n")
    new_lines.extend(lines)
    
    # Call the specific function based on script type
    if script_type == "Python":
        new_lines = add_python_comments(new_lines)
    elif script_type == "PowerShell":
        new_lines = add_powershell_comments(new_lines)
    return new_lines

def add_python_comments(lines):
    new_lines = []
    import_section_added = False
    variable_section_added = False
    map_section_added = False

    for line in lines:
        stripped_line = line.strip()

        # Import section
        if any(re.match(prefix, stripped_line) for prefix in SECTION_MAP["Python"]["import"]) and not import_section_added:
            new_lines.append("\n# Imports\n")
            import_section_added = True

        # Variable section
        elif any(re.match(prefix, stripped_line) for prefix in SECTION_MAP["Python"]["variable"]) and not variable_section_added:
            new_lines.append("\n# Variables\n")
            variable_section_added = True

        # Map section
        elif any(re.match(prefix, stripped_line) for prefix in SECTION_MAP["Python"]["map"]) and not map_section_added:
            new_lines.append("\n# Dictionary\n")
            map_section_added = True

        # Function section
        elif re.match(SECTION_MAP["Python"]["function"], stripped_line) and not line.startswith("    def"):
            new_lines.append("\n# Function\n")

        new_lines.append(line)

    return new_lines

def add_powershell_comments(lines):
    new_lines = []
    import_section_added = False
    variable_section_added = False
    map_section_added = False

    for line in lines:
        stripped_line = line.strip()

        # Import section
        if any(re.match(prefix, stripped_line) for prefix in SECTION_MAP["PowerShell"]["import"]) and not import_section_added:
            new_lines.append("\n# Import\n")
            import_section_added = True

        # Variable section
        elif any(re.match(prefix, stripped_line) for prefix in SECTION_MAP["PowerShell"]["variable"]) and not variable_section_added:
            new_lines.append("\n# Variable\n")
            variable_section_added = True

        # Map section
        elif any(re.match(prefix, stripped_line) for prefix in SECTION_MAP["PowerShell"]["map"]) and not map_section_added:
            new_lines.append("\n# Map\n")
            map_section_added = True

        # Function section
        elif re.match(SECTION_MAP["PowerShell"]["function"], stripped_line) and not line.startswith(" function "):
            new_lines.append("\n# Function\n")

        new_lines.append(line)

    return new_lines