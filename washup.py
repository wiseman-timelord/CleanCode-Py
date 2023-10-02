# Script: washup.py

# COMMENT_MAP
COMMENT_MAP = {
    "Python": "#",
    "PowerShell": "#"
}

# SECTION_MAP
SECTION_MAP = {
    "Python": {
        "import": ["import ", "from "],
        "variable": [" = "],
        "map": [" = {", ": {"],
        "function": "def ",
    },
    "PowerShell": {
        "import": ["Import-Module "],
        "variable": ["$", "$global:"],
        "map": ["@{"],
        "function": "function ",
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
    import_section = False
    function_section = False
    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith(tuple(SECTION_MAP["Python"]["import"])):
            if not import_section:
                new_lines.append("\n# Import\n")
                import_section = True
        # Modified condition to check if stripped line starts with "def "
        elif stripped_line.startswith(SECTION_MAP["Python"]["function"]):
            if not function_section:
                new_lines.append("\n# Function\n")
                function_section = True
            else:
                function_section = False
        new_lines.append(line)
    return new_lines

def add_powershell_comments(lines):
    new_lines = []
    import_section = False
    function_section = False
    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith(tuple(SECTION_MAP["PowerShell"]["import"])):
            if not import_section:
                new_lines.append("\n# Import\n")
                import_section = True
        # Modified condition to check if stripped line starts with "function "
        elif stripped_line.startswith(SECTION_MAP["PowerShell"]["function"]):
            if not function_section:
                new_lines.append("\n# Function\n")
                function_section = True
            else:
                function_section = False
        new_lines.append(line)
    return new_lines
