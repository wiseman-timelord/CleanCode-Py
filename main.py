# main.py

# Imports
import os
import shutil
import time
import sys
from washup import identify_script_type, clean_file_content

# Set window title + size
sys.stdout.write("\x1b]2;Llama2Robot-Window1\x07")
sys.stdout.flush()
if os.name == 'nt':  # Windows
    os.system('mode con: cols=78 lines=44')
else:  # Linux or macOS
    os.system('echo -e "\e[8;44;78t"')
terminal_width = shutil.get_terminal_size().columns

# ANSI color codes
COLOR_RED = "\033[91m"
COLOR_YELLOW = "\033[93m"
COLOR_BLUE = "\033[94m"
COLOR_RESET = "\033[0m"
def print_blue(text):
    print(f"{COLOR_BLUE}{text}{COLOR_RESET}")
def print_yellow(text):
    print(f"{COLOR_YELLOW}{text}{COLOR_RESET}")
def print_red(text):
    print(f"{COLOR_RED}{text}{COLOR_RESET}")

# Ascii Art for the console display
ASCII_ART = r"""   _________            .__        __   _________ .__                        
  /   _____/ ___________|__|______/  |_ \_   ___ \|  |   ____ _____    ____  
  \_____  \_/ ___\_  __ \  \____ \   __\/    \  \/|  | _/ __ \\__  \  /    \ 
  /        \  \___|  | \/  |  |_> >  |  \     \___|  |_\  ___/ / __ \|   |  \
 /_______  /\___  >__|  |__|   __/|__|   \______  /____/\___  >____  /___|  /
         \/     \/         |__|                 \/          \/     \/     \/ """


def center_text(text, width):
    """Center the text within the given width."""
    return text.center(width)

def ensure_directories_exist():
    for dir_name in ["Scripts", "Backup", "Cleaned"]:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

def clean_file(selected_file):
    print_yellow(f"\n Cleaning Script '{selected_file}'...")
    with open(f"./Scripts/{selected_file}", 'r') as f:
        lines = f.readlines()
    total_lines_before = len(lines)
    script_type = identify_script_type(lines)
    print_yellow(f" Identified as {script_type} script.")
    cleaned_lines, lines_removed, comments_removed, blank_lines_removed = clean_file_content(lines, selected_file)
    with open(f"./Cleaned/{selected_file}", 'w') as f:
        f.writelines(cleaned_lines)
    total_lines_after = len(cleaned_lines)
    return lines_removed, comments_removed, blank_lines_removed, total_lines_before, total_lines_after


def clean_and_backup_file(selected_file):
    shutil.copy(f"./Scripts/{selected_file}", f"./Backup/{selected_file}")
    lines_removed, comments_removed, blank_lines_removed, total_lines_before, total_lines_after = clean_file(selected_file)
    os.remove(f"./Scripts/{selected_file}")
    percentage_change = ((total_lines_before - total_lines_after) / total_lines_before) * 100
    print_yellow(f" Removed: {lines_removed} Lines, {blank_lines_removed} Blanks, {comments_removed} Comments")
    print_yellow(f" Difference: {total_lines_before} > {total_lines_after} - {percentage_change:.2f}%")
    time.sleep(2)

def main():
    ensure_directories_exist()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        terminal_width = shutil.get_terminal_size().columns
        equals_line = "=" * 78
        plus_line = "+" * 78
        minus_line = "-" * 78
        centered_ascii_art = center_text(ASCII_ART, terminal_width)
        print_blue(equals_line)
        print_yellow(centered_ascii_art)
        print_blue(equals_line)
        print_blue(plus_line) 
        print_yellow(" Script Operations")
        print_blue(minus_line) 
        print_yellow("\n Scanning Folder...")
        file_types = [f for f in os.listdir("./Scripts") if f.lower().endswith(('.py', '.ps1', '.mql5'))]
        if not file_types:
            print_red(" No Scripts Found!\n")
            print_blue(plus_line)
            return
        print_yellow(" ...Scripts Found.")
        for i, f in enumerate(file_types[:9], start=1):
            print_yellow(f"                             {i}. {f}")
        print_yellow("                             0. Clean All Sripts")
        if len(file_types) > 9:
            print_yellow("\n         ...and more files not shown")
        choice = input(f"\n{COLOR_YELLOW} Select a file to clean (or 'quit' to exit): {COLOR_RESET}")
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
            print_red("Invalid choice.")
            continue

if __name__ == "__main__":
    main()
