# Script: main.py

# Imports
import os
import shutil
import time
import sys
from washup import determine_type, sanitize_script_content
from ascii import ASCII_ART

# Display
sys.stdout.write("\x1b]2;Llama2Robot-Window1\x07")
sys.stdout.flush()
if os.name == 'nt':
    os.system('mode con: cols=78 lines=44')
else:
    os.system('echo -e "\e[8;44;78t"')

# Variables
terminal_width = shutil.get_terminal_size().columns

# Dictionary
COLORS = {
    "RED": "\033[91m",
    "YELLOW": "\033[93m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RESET": "\033[0m"
}

# Function
def display_colored_text(text, color):
    print(f"{COLORS[color]}{text}{COLORS['RESET']}")

# Function
def align_center(text, width):
    """Center the text within the given width."""
    return text.center(width)

# Function
def show_title_header(title="", color="YELLOW", show_ascii=True, mode="menu"):
    equals_line = "=" * 78
    plus_line = "+" * 78
    minus_line = "-" * 78
    if mode == "processing":
        centered_title = "                                 SCRIPT CLEAN"
        display_colored_text(equals_line, "BLUE")
        display_colored_text(centered_title, "YELLOW")
        display_colored_text(equals_line, "BLUE")
        display_colored_text(plus_line, "BLUE")
        display_colored_text(" Processing Scripts:", "YELLOW")
        display_colored_text(minus_line, "BLUE")
        return
    elif mode == "post_processing":
        display_colored_text(plus_line, "BLUE")
        return
    display_colored_text(equals_line, "BLUE")
    if show_ascii:
        centered_ascii_art = align_center(ASCII_ART, terminal_width)
        display_colored_text(centered_ascii_art, "YELLOW")
        display_colored_text(equals_line, "BLUE")
    display_colored_text(plus_line, "BLUE")
    display_colored_text(title, color)
    display_colored_text(minus_line, "BLUE")

# Function
def create_dirs():
    for dir_name in ["Scripts", "Backup", "Cleaned"]:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

# Function
def debug_scripts():
    for filename in os.listdir("./Cleaned"):
        file_path = os.path.join("./Cleaned", filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception:
            pass
    for filename in os.listdir("./Backup"):
        source = os.path.join("./Backup", filename)
        destination = os.path.join("./Scripts", filename)
        try:
            if os.path.isfile(source) or os.path.islink(source):
                shutil.copy2(source, destination)
            elif os.path.isdir(source) and not os.path.exists(destination):
                shutil.copytree(source, destination)
        except Exception:
            pass

# Function
def sanitize_script(selected_file):
    try:
        with open(f"./Scripts/{selected_file}", 'r') as f:
            lines = f.readlines()
        total_lines_before = len(lines)
        script_type = determine_type(selected_file)
        if script_type == "Unknown":
            return (0, 0, 0, 0, 0)
        file_extension = os.path.splitext(selected_file)[1].lstrip('.')
        results = sanitize_script_content(lines, selected_file, file_extension)
        if results:
            cleaned_lines, lines_removed, comments_removed, blank_lines_removed, standard_comments_added = results
        else:
            return (0, 0, 0, 0, 0)
        with open(f"./Cleaned/{selected_file}", 'w') as f:
            f.writelines(cleaned_lines)
        total_lines_after = len(cleaned_lines)
        return lines_removed, comments_removed, blank_lines_removed, total_lines_before, total_lines_after, standard_comments_added
    except Exception as e:
        display_colored_text(f"Error processing the file '{selected_file}': {e}", "RED")
        import traceback
        traceback.print_exc()
        return 0, 0, 0, 0, 0, 0

# Function
def process_script(selected_file):
    try:
        shutil.copy(f"./Scripts/{selected_file}", f"./Backup/{selected_file}")
        lines_removed, comments_removed, blank_lines_removed, total_lines_before, total_lines_after, standard_comments_added = sanitize_script(selected_file)
        os.remove(f"./Scripts/{selected_file}")
        lines_added = total_lines_after - total_lines_before
        comments_added = standard_comments_added
        change = total_lines_before - total_lines_after
        if total_lines_before == 0:
            change_percentage = 0
        else:
            change_percentage = (change / total_lines_before) * 100
        display_colored_text(f"\n Next script from './Scripts' is: '{selected_file}',", "YELLOW")
        display_colored_text(f" Script type is '{determine_type(selected_file)}' with extension '{os.path.splitext(selected_file)[1].lstrip('.')}'.", "YELLOW")
        display_colored_text(f"     Removed: {blank_lines_removed} Blanks, {comments_removed} Comments,", "YELLOW")
        display_colored_text(f"     Added: {lines_added} Blanks, {comments_added} Comments,", "YELLOW")
        display_colored_text(f"     Change: {total_lines_before} > {total_lines_after} = {change_percentage:.2f}%.", "YELLOW")
        time.sleep(2)
    except Exception as e:
        display_colored_text(f"Error: {e}", "RED")

# Function
def main():
    create_dirs()
    while True:
        terminal_width = shutil.get_terminal_size().columns
        show_title_header(" Script Choices:", "YELLOW")
        display_colored_text("\n Scanning Folder...", "YELLOW")
        file_types = [f for f in os.listdir("./Scripts") if f.lower().endswith(('.py', '.bat', '.ps1', '.mql4', '.mql5'))]
        if not file_types:
            display_colored_text(" No Scripts Found!\n                           No Scripts In './Scripts'", "RED")
        else:
            display_colored_text(" ...Scripts Found.", "GREEN")
            for i, f in enumerate(file_types[:9], start=1):
                display_colored_text(f"                             {i}. {f}", "YELLOW")
            display_colored_text("                             0. Clean All Scripts", "YELLOW")
            if len(file_types) > 9:
                display_colored_text("\n         ...and more files not shown", "YELLOW")
        choice = input(f"\n{COLORS['YELLOW']} Select, '0-9' = Choice, 'r' = Re-detect, 'd' = Debug, 'q' = Exit: {COLORS['RESET']}")
        display_colored_text("\n" + "+" * 78, "BLUE")
        if choice.lower() == 'q':
            break
        elif choice.lower() == 'r':
            continue
        elif choice.lower() == 'd':
            debug_scripts()
            continue
        elif choice == '0' and file_types:
            show_title_header(mode="processing")
            for f in file_types:
                process_script(f)
            print()
            show_title_header(mode="post_processing")
            continue
        try:
            show_title_header(mode="processing")
            selected_file = file_types[int(choice) - 1]
            process_script(selected_file)
            print()
            show_title_header(mode="post_processing")
        except (ValueError, IndexError):
            display_colored_text("Invalid choice.", "RED")
            continue

if __name__ == "__main__":
    main()
