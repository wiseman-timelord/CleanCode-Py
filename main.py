# Script: main.py

# Imports
import os
import shutil
import time
import sys
from washup import identify_script_type, clean_file_content
from ascii import ASCII_ART

# Set window title + size
sys.stdout.write("\x1b]2;Llama2Robot-Window1\x07")
sys.stdout.flush()
if os.name == 'nt':  # Windows
    os.system('mode con: cols=78 lines=44')
else:  # Linux or macOS
    os.system('echo -e "\e[8;44;78t"')
terminal_width = shutil.get_terminal_size().columns

# ANSI color codes
COLORS = {
    "RED": "\033[91m",
    "YELLOW": "\033[93m",
    "BLUE": "\033[94m",
    "RESET": "\033[0m"
}

def print_color(text, color):
    print(f"{COLORS[color]}{text}{COLORS['RESET']}")

def center_text(text, width):
    """Center the text within the given width."""
    return text.center(width)

def ensure_directories_exist():
    for dir_name in ["Scripts", "Backup", "Cleaned"]:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

# Function to Clean the File
def clean_file(selected_file):
    try:
        with open(f"./Scripts/{selected_file}", 'r') as f:
            lines = f.readlines()
        total_lines_before = len(lines)
        script_type = identify_script_type(lines)
        print_color(f"\n Identified {script_type} script: '{selected_file}'...", "YELLOW")
        file_extension = os.path.splitext(selected_file)[1].lstrip('.')
        cleaned_lines, lines_removed, comments_removed, blank_lines_removed = clean_file_content(lines, selected_file, file_extension)
        with open(f"./Cleaned/{selected_file}", 'w') as f:
            f.writelines(cleaned_lines)
        total_lines_after = len(cleaned_lines)
        total_blank_and_lines_removed = lines_removed + blank_lines_removed
        print_color(f"     Actions: {total_blank_and_lines_removed} Blanks, {comments_removed} Comments", "YELLOW")
        return lines_removed, comments_removed, blank_lines_removed, total_lines_before, total_lines_after
    except Exception as e:
        print_color(f"Error: {e}", "RED")
        return 0, 0, 0, 0, 0  # Return a default tuple in case of an exception


# Clean and Backup File
def clean_and_backup_file(selected_file):
    try:
        shutil.copy(f"./Scripts/{selected_file}", f"./Backup/{selected_file}")
        lines_removed, comments_removed, blank_lines_removed, total_lines_before, total_lines_after = clean_file(selected_file)
        os.remove(f"./Scripts/{selected_file}")
        print_color(f"     Change: {total_lines_after} > {total_lines_before} = {((total_lines_before - total_lines_after) / total_lines_before) * 100:.2f}%", "YELLOW")
        time.sleep(2)
    except Exception as e:
        print_color(f"Error: {e}", "RED")

def main():
    ensure_directories_exist()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        terminal_width = shutil.get_terminal_size().columns
        equals_line = "=" * 78
        plus_line = "+" * 78
        minus_line = "-" * 78
        centered_ascii_art = center_text(ASCII_ART, terminal_width)
        print_color(equals_line, "BLUE")
        print_color(centered_ascii_art, "YELLOW")
        print_color(equals_line, "BLUE")
        print_color(plus_line, "BLUE") 
        print_color(" Script Choices:", "YELLOW")
        print_color(minus_line, "BLUE") 
        print_color("\n Scanning Folder...", "YELLOW")
        file_types = [f for f in os.listdir("./Scripts") if f.lower().endswith(('.py', '.ps1', '.mql5', '.bat'))]
        if not file_types:
            print_color(" No Scripts Found!", "RED")
            print_color("                             0. Re-Detect Scripts", "YELLOW")
            choice = input(f"\n{COLORS['YELLOW']} Select an option (or 'q' to exit): {COLORS['RESET']}")
            if choice.lower() == 'q':
                print ("")
                print_color(plus_line, "BLUE")
                time.sleep(2)
                break
            elif choice == '0':
                print ("")
                print_color(plus_line, "BLUE")
                time.sleep(2)
                continue
        print_color(" ...Scripts Found.", "YELLOW")
        for i, f in enumerate(file_types[:9], start=1):
            print_color(f"                             {i}. {f}", "YELLOW")
        print_color("                             0. Clean All Sripts", "YELLOW")
        if len(file_types) > 9:
            print_color("\n         ...and more files not shown", "YELLOW")
        choice = input(f"\n{COLORS['YELLOW']} Select an option (or 'q' to exit): {COLORS['RESET']}")
        if choice.lower() == 'q':
            break
        elif choice == '0':
            print ("")
            print_color(plus_line, "BLUE")
            time.sleep(2)
            print_color(plus_line, "BLUE")
            print_color(" Script Operations:", "YELLOW")
            print_color(minus_line, "BLUE") 
            for f in file_types:
                clean_and_backup_file(f)
            continue
        try:
            print ("")
            print_color(plus_line, "BLUE")
            time.sleep(2)
            print_color(plus_line, "BLUE")
            print_color(" Script Operations", "YELLOW")
            print_color(minus_line, "BLUE") 
            selected_file = file_types[int(choice) - 1]
            clean_and_backup_file(selected_file)
        except (ValueError, IndexError):
            print_color("Invalid choice.", "RED")
            continue

if __name__ == "__main__":
    main()
