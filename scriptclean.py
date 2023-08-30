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

def clean_file(selected_file):
    lines_removed = 0
    comments_removed = 0
    blank_lines_removed = 0
    
    print(f"\n Cleaning Script...")
    with open(f"./Scripts/{selected_file}", 'r') as f:
        lines = f.readlines()
    
    total_lines_before = len(lines)
    
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
        
        # Remove inline comments
        if '#' in line:
            parts = line.split('#', 1)
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
    time.sleep(5)

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
