# Script: utility.py

# Imports
import re

# process scripts
def process_script(filename):
    """Processes and cleans the script specified by filename, enhancing with comments."""
    script_type = determine_type(filename)
    if script_type == "Unknown":
        print(f"Skipping unknown script type: {filename}")
        return
    
    # Define paths for the script's lifecycle
    source_path = os.path.join("./Dirty", filename)
    backup_path = os.path.join("./Backup", filename)
    cleaned_path = os.path.join("./Cleaned", filename)
    
    # Backup the script before any processing
    shutil.copy(source_path, backup_path)
    
    # Process and clean the script
    try:
        with open(source_path, 'r', encoding='utf-8') as src_file:
            lines = src_file.readlines()
        
        cleaned_lines = clean_lines(lines, script_type)
        
        with open(cleaned_path, 'w', encoding='utf-8') as cleaned_file:
            cleaned_file.writelines(cleaned_lines)
        
        print(f"Script cleaned and saved: {filename}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")


# remove blank lines
def clean_lines(lines, script_type):
    """Removes comments, empty lines, and inserts section comments based on script type."""
    patterns = SECTION_MAP.get(script_type, {})
    cleaned = []
    for line in lines:
        # Check and remove comments and empty lines
        comment_symbol = COMMENT_MAP.get(script_type, None)
        if comment_symbol and line.strip().startswith(comment_symbol) or not line.strip():
            continue
        
        # Insert comments before sections
        for section, regex_patterns in patterns.items():
            for pattern in regex_patterns:
                if re.match(pattern, line.strip()):
                    section_comment = f"// {section.title()} section\n"
                    if section_comment not in cleaned:
                        cleaned.append(section_comment)
                    break
        
        cleaned.append(line)
    return cleaned
    
# other functions/imports need adjusting for this function to be in utility.
def determine_type(filename):
    file_extension = os.path.splitext(filename)[1].lower()
    return FILE_EXTENSION_TO_TYPE_MAP.get(file_extension, "Unknown")