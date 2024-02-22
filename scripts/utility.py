# Script: utility.py

# Imports
import re, os, datetime, shutil
from pathlib import Path

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

def backup_files(file_type):
    """Backup script or log files based on the file type parameter."""
    try:
        files = []
        backup_path = "./Backup"
        os.makedirs(backup_path, exist_ok=True)  # Ensure backup directory exists

        if file_type == "Script":
            extensions = ('.ps1', '.py', '.bat', '.mq5')
        elif file_type == "Log":
            extensions = ('.log',)

        for filename in os.listdir("./Dirty"):
            if os.path.splitext(filename)[1] in extensions:
                files.append(filename)

        for filename in files:
            source = os.path.join("./Dirty", filename)
            destination = os.path.join(backup_path, filename)
            shutil.copy(source, destination)

        print(f"Backed Up: {len(files)} {file_type}(s)")
    except Exception as e:
        print(f"Backup failed: {e}")

# delete old scripts
def run_old_files_maintenance():
    folders_with_cutoffs = {
        './Backup': datetime.datetime.now() - datetime.timedelta(days=180),  # 6 months
        './Clean': datetime.datetime.now() - datetime.timedelta(days=120),   # 4 months
        './Reject': datetime.datetime.now() - datetime.timedelta(days=60),   # 2 months
    }
    print("Checking Old files..")
    for folder, cutoff_date in folders_with_cutoffs.items():
        old_files = [f for f in Path(folder).iterdir() if f.is_file() and datetime.datetime.fromtimestamp(f.stat().st_mtime) < cutoff_date]
        if old_files:
            print(f"Detected In: {folder}")
            for file in old_files:
                print(f"Removing: {file.name}")
                file.unlink()  # Removes the file
        else:
            print(f"Checked: {folder}")
    print("..Maintenance done.\n")

# remove unsupported
def run_remove_unsupported_files():
    allowed_extensions = ['.ps1', '.py', '.bat', '.mq5', '.log']
    script_files = Path("./Dirty").glob("*.*")
    unsupported_files = [f for f in script_files if f.suffix.lower() not in allowed_extensions]
    print("Checking ./Dirty Folder..")
    if unsupported_files:
        print("..Unsupported Scripts!")
        for file in unsupported_files:
            destination = Path("./Reject") / file.name
            shutil.move(str(file), str(destination))
            print(f"Rejected: {file.name}")
    else:
        print("..All scripts supported.")
    print("")