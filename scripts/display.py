# Script: display.py

# Imports
import os, time, sys
from Color_Console import color

# Function clear_screen
def clear_screen():
    os.system('cls')

# Function set_default_colors
def set_default_colors():
    print("Configuring Display..")
    time.sleep(1)
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
        script_extensions = ('.ps1', '.py', '.bat', '.mq5')
        log_extension = '.log'
        script_files = [f for f in os.listdir("./Dirty") if os.path.splitext(f)[1].lower() in [ext.lower() for ext in script_extensions]]
        log_files = [f for f in os.listdir("./Dirty") if os.path.splitext(f)[1].lower() == log_extension.lower()]
        script_count = len(script_files)
        log_count = len(log_files)
        print("\n\n\n\n\n\n\n\n")
        print(f"                       1. Clean Scripts,")
        print(f"                            ({script_count} Found)\n")
        print(f"                       2. Clean Logs.")
        print(f"                            ({log_count} Found)")
        print("\n\n\n\n\n\n\n\n\n")
        draw_separator()
        print("Select; Options = 1-2, Reload = R, Exit = X: ", end='')
        choice = input().strip().lower()
        if choice == 'x':
            print("Exit Initiated...")
            time.sleep(2)
            break
        elif choice == 'r':
            print("Refreshing Display...")
            time.sleep(2)
            continue
        else:
            from scripts.utility import clean_scripts, clean_logs
            if choice == '1':
                print("Cleaning scripts...")
                time.sleep(2)
                clean_scripts()
            elif choice == '2':
                print("Cleaning Logs...")
                time.sleep(2)
                clean_logs()
            else:
                print("Invalid choice, please try again.")
                time.sleep(2)

