# Script: cleaner.py

# process scripts
def process_script(filename):
    """Processes and cleans the script specified by filename."""
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
    """Removes comments and empty lines based on script type."""
    comment_symbol = COMMENT_MAP.get(script_type, None)
    if not comment_symbol:
        return lines

    cleaned = []
    for line in lines:
        if not line.strip().startswith(comment_symbol) and line.strip():
            cleaned.append(line)
    return cleaned