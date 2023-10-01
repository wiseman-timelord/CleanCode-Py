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
        "global-variables": [" = ", " = None", " = []", " = {}"],  # Added this line
        "dictionaries": [" = {", ": {"],  # Added this line
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
    # Enhanced check for script type
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

def clean_file_content(lines, script_name, file_extension):
    script_type = identify_script_type(lines)
    if script_type == "Unknown":
        print("Warning: Unknown script type. No changes made.")
        return lines, 0, 0, 0

    # Remove all comments
    lines = [line for line in lines if not line.strip().startswith(COMMENT_MAP[script_type])]
    
    # Remove all blank lines
    lines = [line for line in lines if line.strip() != ""]
    
    # Add comments before sections and blank lines after
    cleaned_lines = add_standard_comments(lines, script_type, script_name, file_extension)
    
    lines_removed = len(lines) - len(cleaned_lines)
    blank_lines_removed = sum(1 for line in lines if not line.strip()) - sum(1 for line in cleaned_lines if not line.strip())
    comments_removed = sum(1 for line in lines if line.strip().startswith(COMMENT_MAP[script_type])) - sum(1 for line in cleaned_lines if line.strip().startswith(COMMENT_MAP[script_type]))
    
    return cleaned_lines, lines_removed, blank_lines_removed, comments_removed

def add_standard_comments(lines, script_type, script_name, file_extension):
    new_lines = []
    if not lines:
        return []
    comment_prefix = COMMENT_MAP.get(script_type, "//")
    
    # Add the script title comment
    new_lines.append(f"{comment_prefix} Script: {script_name}\n")
    
    prev_section = None
    for i, line in enumerate(lines):
        current_section = None
        for section, identifier in SECTION_MAP[script_type].items():
            if isinstance(identifier, list):
                if any(line.lstrip().startswith(iden) for iden in identifier):
                    current_section = section
                    break
            else:
                if line.lstrip().startswith(identifier):
                    current_section = section
                    break
        
        # Add the section comment if the line is in the global scope (not indented)
        if current_section and current_section != prev_section and not line.startswith("    "):  # Assuming 4 spaces for indentation
            new_lines.append("\n")  # Add a blank line before the comment
            # Properly format the section name
            section_name = current_section.replace("-", " ").capitalize()
            if section_name == "Import":
                section_name = "Imports"
            elif section_name == "Dictionaries":
                section_name = "Dictionary" if lines[i+1].count("{") == 1 else "Dictionaries"
            new_lines.append(f"{comment_prefix} {section_name}\n")
        
        new_lines.append(line)
        
        prev_section = current_section
    
    # Remove any duplicate consecutive newlines
    final_lines = [new_lines[0]]
    for i in range(1, len(new_lines)):
        if new_lines[i] == "\n" and new_lines[i-1] == "\n":
            continue
        final_lines.append(new_lines[i])
    
    return final_lines


