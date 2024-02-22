# Script: display.py

from scripts.utility import process_script, backup_files
import os, time, sys
from Color_Console import color

# Function clear_screen
def clear_screen():
    os.system('cls')

# Function set_default_colors
def set_default_colors():
    print("Configuring Display..")
    sys.stdout.flush()
    color(text="bright white", bg="gray")
    clear_screen()
    draw_title()
    print("Initializing Program...\n")
    print("Configuring Display..")
    print("..Display Configured.\n")

# Function draw_title
def draw_title():
    print("\n=========================( CleanCode-Py )=========================\n")

# Function draw_separator
def draw_separator():
    print("\n------------------------------------------------------------------")

# Function show_main_menu
def show_main_menu():
    while True:
        clear_screen()
        draw_title()
        
        # Updated logic to match PowerShell version
        script_extensions = ('.ps1', '.py', '.bat', '.mq5')
        log_extension = '.log'
        script_files = [f for f in os.listdir("./Dirty") if os.path.splitext(f)[1] in script_extensions]
        log_files = [f for f in os.listdir("./Dirty") if os.path.splitext(f)[1] == log_extension]
        script_count = len(script_files)
        log_count = len(log_files)

        print("\n\n\n\n\n\n\n\n\n")  # Match the spacing in PowerShell version
        print(f"                       1. Clean Scripts,")
        print(f"                            ({script_count} Found)\n")
        print(f"                       2. Clean Logs.")
        print(f"                            ({log_count} Found)")
        print("\n\n\n\n\n\n\n\n\n")
        draw_separator()
        choice = input("Select; Options = 1-2, Reload = R, Exit = X: ").strip().lower()

        if choice == 'x':
            print("Exit Initiated...")
            time.sleep(2)
            break
        elif choice == 'r':
            print("Refreshing Display...")
            time.sleep(2)
            continue 
        elif choice == '1':
            print("Backing up Scripts...")
            backup_files("Script")  # Adjusted to pass file type
            print("Processing Scripts...")
            for filename in script_files:
                process_script(filename)
            time.sleep(2)
        elif choice == '2':
            print("Backing up Logs...")
            backup_files("Log")  # Adjusted to pass file type
            print("Processing Logs...")
            # Ensure you have a function to handle log processing
            for filename in log_files:
                process_log(filename)  # This function needs to be implemented
            time.sleep(2)
        else:
            print("Invalid choice, please try again.")
            time.sleep(2)
