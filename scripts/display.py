# Script: display.py

from scripts.utility import process_script
import os, time

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def set_default_colors():
    print("Configuring Display..")
    sys.stdout.write('\033[37;100m')
    sys.stdout.flush()
    # Clear screen and re-print
    clear_screen()
    print("Configuring Display..")
    print("..Display Configured.")

def draw_title():
    print("\n=========================( CleanCode-Py )=========================\n")
    
def draw_separator():
    print("\n------------------------------------------------------------------")

def show_main_menu():
    while True:
        clear_screen()
        draw_title()
        print("1. Clean Scripts")
        print("2. Clean Logs")
        draw_separator()
        choice = input("Select; Options = 1-2, Reload = R, Debug = D, Exit = X: ").strip().lower()

        if choice == 'x':
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

