# Script: display.py

from scripts.cleaner import process_script
import os, time

def clear_screen():
    """Clears the terminal screen."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def show_main_menu():
    """Displays the main menu options to the user and handles all user interactions."""
    create_dirs()  # Ensure necessary directories exist at the start.
    while True:
        clear_screen()
        print("Main Menu:")
        print("1. Option 1")
        print("2. Option 2")
        choice = input("Select, '0-9' = Choice, 'r' = Re-detect, 'd' = Debug, 'q' = Exit: ").strip().lower()

        if choice == 'q':
            break
        elif choice == 'r':
            continue 
        elif choice == 'd':
            debug_scripts() 
            time.sleep(2)
        elif choice.isdigit() and int(choice) in range(1, 10):
            filenames = [f for f in os.listdir("./Dirty") if f.endswith(tuple(FILE_EXTENSION_TO_TYPE_MAP.keys()))]
            if 0 < int(choice) <= len(filenames):
                process_script(filenames[int(choice) - 1])
            else:
                print("Invalid choice.")
                time.sleep(2)

        else:
            print("Invalid choice.")
            time.sleep(2)

