# Script: utility.py

# Imports
import re, os, datetime, shutil, time
from pathlib import Path
from scripts.maps import COMMENT_MAP, SECTION_MAP, FILE_EXTENSION_TO_TYPE_MAP, FOLDERS_WITH_CUTOFFS

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
    run_remove_unsupported_files()
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
        entry_comment = "# Entry Point" if any("entry" in line.lower() and COMMENT_MAP.get(script_type, "") in line for line in lines) else None
        cleaned_lines = clean_lines(lines, script_type)
        if entry_comment:
            insert_index = find_insertion_index(cleaned_lines, script_type)
            cleaned_lines.insert(insert_index, "\n" + entry_comment)
        with open(cleaned_path, 'w', encoding='utf-8') as cleaned_file:
            cleaned_file.writelines(cleaned_lines)
        print(f"Script cleaned and saved: {filename}")
        time.sleep(1)
    except Exception as e:
        print(f"Error processing {filename}: {e}")
        time.sleep(1)

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
        for section, regex_patterns in patterns.items():
            matched_section = next((pattern for pattern in regex_patterns if re.match(pattern, line.strip())), None)
            if matched_section:
                section_comment = f"{comment_symbol} {section.title()}\n"
                if section_comment not in cleaned:
                    cleaned.append(section_comment)
                break
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
    """Backup script or log files based on the file type parameter."""
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

# Function run_remove_unsupported_files
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