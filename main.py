# Script: main.py

# Imports
import os, shutil, sys, time, datetime
from scripts.display import show_main_menu, clear_screen, draw_title, set_default_colors
from scripts.utility import process_script, run_old_files_maintenance, run_remove_unsupported_files
from scripts.maps import FOLDERS_WITH_CUTOFFS
from Color_Console import color

# Global Variables
terminal_width = shutil.get_terminal_size().columns

# Function finalize_program
def initialize_program():
    clear_screen()
    draw_title()
    print("Initializing Program...\n")
    time.sleep(1)
    set_default_colors()
    time.sleep(1)
    run_old_files_maintenance(FOLDERS_WITH_CUTOFFS)
    time.sleep(1)
    run_remove_unsupported_files()
    time.sleep(1)
    print("...Program Initialized.\n")
    time.sleep(2)

# Function finalize_program
def finalize_program():
    draw_title()
    print("Finalizing Program...\n")
    print("\n...Program Finalized.")
    exit()


# Entry Point
if __name__ == "__main__":
    initialize_program()
    show_main_menu()
    finalize_program()