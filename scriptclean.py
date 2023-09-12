import os
import shutil
import time

# Ascii Art for the console display
ASCII_ART = r"""  _________            .__        __   _________ .__                        
 /   _____/ ___________|__|______/  |_ \_   ___ \|  |   ____ _____    ____  
 \_____  \_/ ___\_  __ \  \____ \   __\/    \  \/|  | _/ __ \\__  \  /    \ 
 /        \  \___|  | \/  |  |_> >  |  \     \___|  |_\  ___/ / __ \|   |  \
/_______  /\___  >__|  |__|   __/|__|   \______  /____/\___  >____  /___|  /
        \/     \/         |__|                 \/          \/     \/     \/ """



def ensure_directories_exist():
    for dir_name in ["Scripts", "Backup", "Cleaned"]:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

def identify_script_type(lines):
    # Counters for different script types
    python_count = 0
    powershell_count = 0
    cpp_count = 0
    batch_count = 0
    
    for line in lines:
        if line.startswith("def "):
            python_count += 1
        elif line.startswith("echo "):
            batch_count += 1
        elif line.startswith("function "):
            powershell_count += 1
        elif line.startswith("#include "):
            cpp_count += 1
    
    # Identify the script type based on the counters
    max_count = max(python_count, powershell_count, cpp_count, batch_count)
    
    if max_count == python_count:
        return "Python"
    elif max_count == powershell_count:
        return "PowerShell"
    elif max_count == cpp_count:
        return "C++"
    elif max_count == batch_count:
        return "Batch"
    else:
        return "Unknown"

def add_comments_to_python_script(lines):
    new_lines = []
    for i, line in enumerate(lines):
        if i > 0 and line.startswith("def ") and not lines[i-1].lstrip().startswith("#"):
            new_lines.append("# function\n")
        elif i > 0 and line.startswith("class ") and not lines[i-1].lstrip().startswith("#"):
            new_lines.append("# class\n")
        new_lines.append(line)
    return new_lines

def clean_file(selected_file):
    lines_removed = 0
    comments_removed = 0
    blank_lines_removed = 0
    
    print(f"\n Cleaning Script '{selected_file}'...")
    with open(f"./Scripts/{selected_file}", 'r') as f:
        lines = f.readlines()
    
    total_lines_before = len(lines)
    
    # Identify the script type
    script_type = identify_script_type(lines)
    print(f" Identified as {script_type} script.")
    
    # Add comments to Python script if needed
    if script_type == "Python":
        lines = add_comments_to_python_script(lines)
    
    cleaned_lines = []
    
    for i, line in enumerate(lines):
        # Look ahead to the next line if available
        next_line = lines[i + 1] if i + 1 < len(lines) else None
        
        # Remove lines with only spaces
        if line.strip() == '':
            if next_line is None or next_line.strip() == '' or next_line.startswith(' '):
                blank_lines_removed += 1
                continue
        
        # Remove lines starting with one or more spaces followed by #
        if line.lstrip().startswith('#') and line.lstrip() != line:
            lines_removed += 1
            continue
        
        # Remove inline comments based on new rule
        if '# ' in line and not line.lstrip().startswith('# '):
            if '##' not in line and '###' not in line:
                parts = line.split('# ', 1)
                if parts[0].strip() != '':
                    line = parts[0] + '\n'
                    comments_removed += 1
        
        cleaned_lines.append(line)
    
    with open(f"./Cleaned/{selected_file}", 'w') as f:
        f.writelines(cleaned_lines)
    
    total_lines_after = len(cleaned_lines)
    
    return lines_removed, comments_removed, blank_lines_removed, total_lines_before, total_lines_after


def clean_and_backup_file(selected_file):
    shutil.copy(f"./Scripts/{selected_file}", f"./Backup/{selected_file}")
    lines_removed, comments_removed, blank_lines_removed, total_lines_before, total_lines_after = clean_file(selected_file)
    os.remove(f"./Scripts/{selected_file}")
    percentage_change = ((total_lines_before - total_lines_after) / total_lines_before) * 100
    print(f" Removed: {lines_removed} Lines, {blank_lines_removed} Blanks, {comments_removed} Comments")
    print(f" Difference: {total_lines_before} > {total_lines_after} - {percentage_change:.2f}%")
    time.sleep(2)

def main():
    ensure_directories_exist()
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("="*76)
        print(ASCII_ART)
        print("="*76)
        print("\n Scanning Folder...")
        
        file_types = [f for f in os.listdir("./Scripts") if f.endswith(('.py', '.ps1'))]
        
        if not file_types:
            print(" No Scripts Found!\n")
            return
        
        print(" ...Scripts Found.")
        
        # Display only the first 9 files in the menu
        for i, f in enumerate(file_types[:9], start=1):
            print(f"                             {i}. {f}")
        
        # Show option for cleaning all files
        print("                             0. Clean All Sripts")
        
        # Show overflow files if any
        if len(file_types) > 9:
            print("\n         ...and more files not shown")
        
        choice = input("\n Select a file to clean (or 'quit' to exit): ")
        
        if choice.lower() == 'quit':
            return
        elif choice == '0':
            for f in file_types:
                clean_and_backup_file(f)
            continue
        
        try:
            selected_file = file_types[int(choice) - 1]
            clean_and_backup_file(selected_file)
        except (ValueError, IndexError):
            print("Invalid choice.")
            continue

if __name__ == "__main__":
    main()
