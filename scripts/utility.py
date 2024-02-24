# Script: utility.py

# Imports
import re, os, datetime, shutil, time
from pathlib import Path
from scripts.maps import COMMENT_MAP, SECTION_MAP, FILE_EXTENSION_TO_TYPE_MAP, FOLDERS_WITH_CUTOFFS
from scripts.display import clear_screen, draw_title, draw_separator


def clean_scripts():
    print("Cleaning Scripts...")
    clear_screen()
    draw_title()
    run_remove_unsupported_files()
    backup_files("Script")
    script_files = [f for f in os.listdir("./Dirty") if os.path.splitext(f)[1] in ('.ps1', '.py', '.bat', '.mq5')]
    print("Processing Scripts...")
    for filename in script_files:
        process_script(filename)
    print("\n...Scripts Cleaned.")
    draw_separator()
    print("Returning To Menu...")
    time.sleep(2)


def clean_logs():
    print("Cleaning Logs...")
    clear_screen()
    draw_title()
    run_remove_unsupported_files()
    backup_files("Log")
    log_files = [f for f in os.listdir("./Dirty") if os.path.splitext(f)[1] == '.log']
    print("Processing Logs...")
    for filename in log_files:
        process_logs(filename)
    print("\n...Logs Cleaned.")
    draw_separator()
    print("Returning To Menu...")
    time.sleep(2)


def process_file(filename):
    file_extension = os.path.splitext(filename)[1].lower()
    if file_extension in ['.ps1', '.py', '.bat', '.mq5']:
        process_script(filename)
    elif file_extension == '.log':
        process_logs(filename)
    else:
        print(f"Unsupported file type for {filename}. Skipping...")

# Function determine_type
def determine_type(filename):
    file_extension = os.path.splitext(filename)[1].lower()
    return FILE_EXTENSION_TO_TYPE_MAP.get(file_extension, "Unknown")

# Function process_scripts
def process_script(filename):
    script_type = determine_type(filename)
    if script_type == "Unknown":
        print(f"Skipping unknown script type: {filename}")
        return
    source_path = os.path.join("./Dirty", filename)
    backup_path = os.path.join("./Backup", filename)
    cleaned_path = os.path.join("./Clean", filename)
    shutil.copy(source_path, backup_path)
    try:
        with open(source_path, 'r', encoding='utf-8') as src_file:
            lines = src_file.readlines()
        
        # Counting before cleaning
        total_lines_before = len(lines)
        blanks_before = sum(1 for line in lines if not line.strip())
        comments_before = sum(1 for line in lines if line.strip().startswith(COMMENT_MAP.get(script_type, "#")))
        
        entry_comment = "# Entry Point" if any("entry" in line.lower() and COMMENT_MAP.get(script_type, "") in line for line in lines) else None
        cleaned_lines = clean_lines(lines, script_type)
        
        if entry_comment:
            insert_index = find_insertion_index(cleaned_lines, script_type)
            cleaned_lines.insert(insert_index, "\n" + entry_comment)
            
        # Counting after cleaning
        total_lines_after = len(cleaned_lines)
        blanks_after = sum(1 for line in cleaned_lines if not line.strip())
        comments_after = sum(1 for line in cleaned_lines if line.strip().startswith(COMMENT_MAP.get(script_type, "#")))
        
        with open(cleaned_path, 'w', encoding='utf-8') as cleaned_file:
            cleaned_file.writelines(cleaned_lines)
        
        # Calculating reduction
        reduction_percentage = (1 - total_lines_after / total_lines_before) * 100 if total_lines_before else 0
        
        print(f"\nCleaning Script: {filename}")
        print(f"Before: Blanks={blanks_before}, Comments={comments_before}, Lines={total_lines_before}")
        print(f"After: Blanks={blanks_after}, Comments={comments_after}, Lines={total_lines_after}")
        print(f"Reduction: {reduction_percentage:.2f}%")
        time.sleep(1)
        
    except Exception as e:
        print(f"Error processing {filename}: {e}")


# Function process_logs
def process_logs(filename):
    run_remove_unsupported_files()
    print(f"Cleaning log file: {filename}")
    time.sleep(1)
    source_path = os.path.join("./Dirty", filename)
    try:
        ansi_escape_pattern = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
        with open(source_path, 'r', encoding='utf-8') as log_file:
            filtered_content = [ansi_escape_pattern.sub('', line) for line in log_file]
        with open(source_path, 'w', encoding='utf-8') as log_file:
            log_file.writelines(filtered_content)
        print(f"Log file cleaned: {filename}")
    except Exception as e:
        print(f"Error cleaning log file {filename}: {e}")

# Function clean_lines
def clean_lines(lines, script_type):
    comment_symbol = COMMENT_MAP.get(script_type, "#")
    patterns = SECTION_MAP.get(script_type, {})
    cleaned = []
    
    for line in lines:
        if line.strip().startswith(comment_symbol) or not line.strip():
            continue
        found_section = False
        for section, regex_patterns in patterns.items():
            for pattern in regex_patterns:
                if re.match(pattern, line.strip()):
                    section_comment = f"{comment_symbol} {section.title()}\n"
                    if section_comment not in cleaned:
                        cleaned.append(section_comment)  # Add section comment once
                    found_section = True
                    break
            if found_section:
                break
        if not found_section:
            cleaned.append(line) 
    return cleaned
    
# Function find_insertion_index
def find_insertion_index(cleaned_lines, script_type):
    insert_index = len(cleaned_lines)
    patterns = SECTION_MAP.get(script_type, {})
    for section, regex_patterns in patterns.items():
        for pattern in regex_patterns:
            for i, line in enumerate(cleaned_lines):
                if re.match(pattern, line.strip()):
                    insert_index = min(insert_index, i)
                    break
            if insert_index != len(cleaned_lines):
                break
    return 0 if insert_index == len(cleaned_lines) else insert_index

# Function clean_log_files
def clean_log_files():
    log_files = [f for f in os.listdir("./Dirty") if f.endswith('.log')]
    for filename in log_files:
        process_logs(filename)

# Function backup_files
def backup_files(file_type):
    print("Backing Up Scripts..")
    try:
        files = []
        backup_path = "./Backup"
        os.makedirs(backup_path, exist_ok=True)
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
    print("..Scripts Backed Up.\n")
    time.sleep(1)

# Function run_remove_unsupported_files
def run_remove_unsupported_files():
    print("Checking File Types..")
    allowed_extensions = ['.ps1', '.py', '.bat', '.mq5', '.log']
    script_files = Path("./Dirty").glob("*.*")
    unsupported_files = [f for f in script_files if f.suffix.lower() not in allowed_extensions]
    print("..Checking ./Dirty Folder..")
    if unsupported_files:
        print("..Unsupported Scripts!")
        for file in unsupported_files:
            destination = Path("./Reject") / file.name
            shutil.move(str(file), str(destination))
            print(f"Rejected: {file.name}")
    else:
        print("..All scripts supported.")
    print("")
    time.sleep(1)

# Function run_old_files_maintenance
def run_old_files_maintenance(FOLDERS_WITH_CUTOFFS):
    print("Checking Old files..")
    for folder, cutoff_date in FOLDERS_WITH_CUTOFFS.items():
        old_files = [f for f in Path(folder).iterdir() if f.is_file() and datetime.datetime.fromtimestamp(f.stat().st_mtime) < cutoff_date]
        if old_files:
            print(f"Detected In: {folder}")
            for file in old_files:
                print(f"Removing: {file.name}")
                file.unlink()
        else:
            print(f"Checked: {folder}")
    print("..Maintenance done.\n")
    time.sleep(1)