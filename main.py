from db import init_db
from ui import main_menu, add_task_ui, mark_task_as_done_ui, view_tasks_ui, view_done_ui, filter_tasks_ui, view_motto_desire_ui, view_task_description
import os

def clear_screen():
    # Clear the screen for Windows and Unix-based systems
    os.system('cls' if os.name == 'nt' else 'clear')
    
def main():
    init_db()

    while True:
        choice = main_menu()

        if choice == '1':
            clear_screen()
            add_task_ui()
        elif choice == '2':
            clear_screen()
            view_tasks_ui()
        elif choice == '3':
            clear_screen()
            mark_task_as_done_ui()
        elif choice == '4':
            clear_screen()
            filter_tasks_ui()
        elif choice == '5':
            clear_screen()
            view_done_ui()
        elif choice == '6':
            clear_screen()
            view_motto_desire_ui()
        elif choice == '7':
            clear_screen()
            view_task_description()
        elif choice == '8':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
        

if __name__ == "__main__":
    main()
