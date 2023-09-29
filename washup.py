# Maps
COMMENT_MAP = {
    "Python": "#",
    "PowerShell": "#",
    "Batch": "REM",
    "MQL5": "//"
}

SECTION_MAP = {
    "Python": {
        "import": "import ",
        "from-import": "from ",
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

def add_standard_comments(lines, script_type, script_name):
    new_lines = []
    comment_prefix = COMMENT_MAP.get(script_type, "//")
    
    # Check if the script name is already present in the first line
    if not lines[0].strip().endswith(f"Script: {script_name}"):
        new_lines.append(f"{comment_prefix} Script: {script_name}\n")
    prev_section = None
    for i, line in enumerate(lines):
        current_section = None
        for section, identifier in SECTION_MAP[script_type].items():
            if isinstance(identifier, list):
                if any(line.startswith(iden) for iden in identifier):
                    current_section = section
                    break
            else:
                if line.startswith(identifier):
                    current_section = section
                    break
        if current_section and current_section != prev_section and (i == 0 or not lines[i-1].lstrip().startswith(comment_prefix)):
            new_lines.append(f"{comment_prefix} {current_section.capitalize()}\n")
        new_lines.append(line)
        prev_section = current_section
    return new_lines

def clean_file_content(lines, script_name):
    script_type = identify_script_type(lines)
    cleaned_lines = add_standard_comments(lines, script_type, script_name)
    total_lines_before = len(lines)
    total_lines_after = len(cleaned_lines)
    lines_removed = total_lines_before - total_lines_after
    comments_removed = sum(1 for line in lines if line.strip().startswith(COMMENT_MAP.get(script_type, "//")))
    blank_lines_removed = sum(1 for line in lines if not line.strip())
    return cleaned_lines, lines_removed, comments_removed, blank_lines_removed
