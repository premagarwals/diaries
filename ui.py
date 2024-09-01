from colorama import Fore, Style, init
init()

def print_header(header):
    print(Fore.GREEN + Style.BRIGHT + header + Style.RESET_ALL)

def print_todo(task):
    print(Fore.CYAN + f"[{task[0]}] Todo: {task[1]}" + Style.RESET_ALL)
    print(Fore.WHITE + f"   {task[4]}" + Style.RESET_ALL)
    print(Fore.YELLOW + f"Status: {task[5]}" + Style.RESET_ALL)
    if len(task) > 7:  # Check if description is present
        print(Fore.MAGENTA + f"Start: {task[7]}" + Style.RESET_ALL)
        print(Fore.MAGENTA + f"Deadline: {task[8]}" + Style.RESET_ALL)
    print()

def print_project(task):
    print(Fore.CYAN + f"[{task[0]}] Project: {task[1]}" + Style.RESET_ALL)
    print(Fore.WHITE + f"   {task[4]}\n" + Style.RESET_ALL)
    print(Fore.YELLOW + f"Status: {task[5]}" + Style.RESET_ALL)
    print(Fore.BLUE + f"Assigned: {task[6]}" + Style.RESET_ALL)
    if len(task) > 7:  # Check if description is present
        print(Fore.MAGENTA + f"Start: {task[7]}" + Style.RESET_ALL)
        print(Fore.MAGENTA + f"Deadline: {task[8]}" + Style.RESET_ALL)
        print(Fore.GREEN + f"[+] Completed: {task[9]}" + Style.RESET_ALL)
    print()

def print_achievment(task):
    print(Fore.CYAN + f"[{task[0]}] Achievement: {task[1]}" + Style.RESET_ALL)
    print(Fore.YELLOW + f"Status: {task[5]}" + Style.RESET_ALL)
    print(Fore.BLUE + f"Assigned: {task[6]}" + Style.RESET_ALL)
    print(Fore.WHITE + f"   {task[4]}" + Style.RESET_ALL)
    print()

def print_motto(task):
    print(Fore.CYAN + f"[{task[0]}] Motto: {task[1]}" + Style.RESET_ALL)
    print(Fore.YELLOW + f"Status: {task[5]}" + Style.RESET_ALL)
    print(Fore.BLUE + f"Wished on: {task[7]}" + Style.RESET_ALL)
    print(Fore.WHITE + f"   {task[4]}\n" + Style.RESET_ALL)
    print(Fore.GREEN + f"[+] Completed: {task[9]}" + Style.RESET_ALL)
    print()

def main_menu():
    print("\n\nWelcome to Your To-Achieve App!")
    print("--------------------------------")
    print("[1] Add New Task")
    print("[2] View All Tasks")
    print("[3] Mark Task as Done")
    print("[4] Filter Tasks")
    print("[5] View Achievements")
    print("[6] View Motto/Desire")
    print("[7] View Description")
    print("[8] Exit")
    print("--------------------------------")
    choice = input("Choose an option: ")
    return choice

from datetime import datetime, timedelta

def add_task_ui():
    print("\n--- Add New Task ---")
    title = input("Enter task title: ")

    print("Select task type:")
    print("[1] Project")
    print("[2] To-Do")
    print("[3] Achievement")
    print("[4] Motto/Desire")
    task_type_options = {1: 'Project', 2: 'To-Do', 3: 'Achievement', 4: 'Motto/Desire'}
    task_type_choice = int(input("Enter number: "))
    task_type = task_type_options.get(task_type_choice, 'To-Do')

    print("Select category:")
    print("[1] Academics")
    print("[2] Health")
    print("[3] Passion")
    print("[4] Career")
    print("[5] Entertainment")
    category_options = {1: 'Academics', 2: 'Health', 3: 'Passion', 4: 'Career', 5: 'Entertainment'}
    category_choice = int(input("Enter number: "))
    category = category_options.get(category_choice, 'Entertainment')

    description = input("Enter a description: ")
    if task_type_choice == 1 or task_type_choice == 4:
        start_date = input("Enter start date (YYYY-MM-DD) or leave blank for today: ")
        if task_type_choice == 1:
            end_date = input("Enter target deadline (YYYY-MM-DD) or leave blank for today: ")
        else:
            end_date = "XXXX-XX-XX"
        date_assigned = input("Enter date assigned (YYYY-MM-DD) or leave blank for today: ")
    elif task_type_choice == 2 or task_type_choice == 3:
        start_date = input("Enter start date (YYYY-MM-DD) or leave blank for today: ")
        end_date = start_date
        date_assigned = datetime.now().strftime('%Y-%m-%d')
        
    

    if start_date.startswith('~'):
        start_date = (datetime.now() + timedelta(days=int(start_date[1:]))).strftime('%Y-%m-%d')
    if end_date.startswith('~'):
        end_date = (datetime.now() + timedelta(days=int(end_date[1:]))).strftime('%Y-%m-%d')
    if not date_assigned:
        date_assigned = datetime.now().strftime('%Y-%m-%d')

    from db import add_task
    if task_type_choice == 3:
        add_task(title, task_type, category, description, date_assigned, start_date, end_date, status="Done")
    else:
        add_task(title, task_type, category, description, date_assigned, start_date, end_date)

    print("Task added successfully!\n")


# Additional UI functions will be added as we proceed...

def mark_task_as_done_ui():
    task_id = input("Enter the ID of the task to mark as done: ")
    
    from db import mark_task_as_done
    mark_task_as_done(int(task_id))
    
    print(f"Task {task_id} marked as done!\n")

def view_tasks_ui():
    print("\n--- View Tasks ---")

    from db import view_all_tasks
    tasks = view_all_tasks()

    if not tasks:
        print("No tasks found.\n")
        return

    # Group tasks by type
    todos = [task for task in tasks if task[2] == 'To-Do' and task[5] == 'Not Done']
    projects = [task for task in tasks if task[2] == 'Project' and task[5] == 'Not Done']
    mottos = [task for task in tasks if task[2] == 'Motto/Desire' and task[5] == 'Not Done']
    achievements = [task for task in tasks if task[2] == 'Achievement' and task[5] == 'Not Done']

    # Display To-Dos first
    print("\n--- To-Do Tasks ---")
    for task in todos:
        print_todo(task)

    # Display Projects
    print("\n--- Project Tasks ---")
    for task in projects:
        print_project(task)

    # Display Mottos
    print("\n--- Motto/Desire Tasks ---")
    for task in mottos:
        print_motto(task)

    # Display Achievements
    print("\n--- Achievements ---")
    for task in achievements:
        print_achievment(task)

def view_done_ui():
    print(Fore.GREEN + Style.BRIGHT + "\n--- View Tasks ---" + Style.RESET_ALL)

    from db import view_all_tasks
    tasks = view_all_tasks()
    tasks = [task for task in tasks if task[5] == 'Done']
    if not tasks:
        print(Fore.RED + "No tasks found." + Style.RESET_ALL)
        return

    todos = [task for task in tasks if task[2] == 'To-Do']
    projects = [task for task in tasks if task[2] == 'Project']
    mottos = [task for task in tasks if task[2] == 'Motto/Desire']
    achievements = [task for task in tasks if task[2] == 'Achievement']

    # Display To-Dos first
    print("\n--- To-Do Tasks ---")
    for task in todos:
        print_todo(task)

    # Display Projects
    print("\n--- Project Tasks ---")
    for task in projects:
        print_project(task)

    # Display Mottos
    print("\n--- Motto/Desire Tasks ---")
    for task in mottos:
        print_motto(task)

    # Display Achievements
    print("\n--- Achievements ---")
    for task in achievements:
        print_achievment(task)


def filter_tasks_ui():
    print(Fore.CYAN + Style.BRIGHT + "\n--- Filter Tasks ---" + Style.RESET_ALL)
    
    # Display options for task type filtering
    print(Fore.YELLOW + "Select task type to filter by:" + Style.RESET_ALL)
    print("[1] To-Do")
    print("[2] Project")
    print("[3] Achievement")
    print("[4] Motto/Desire")
    
    from db import filter_tasks_by_type, filter_tasks_by_category
    try:
        task_type_choice = int(input("Enter the number for task type: "))
        filtered_tasks_by_type = filter_tasks_by_type(task_type_choice)
        
        if filtered_tasks_by_type:
            print(Fore.GREEN + Style.BRIGHT + "\nFiltered Tasks by Type:" + Style.RESET_ALL)
            for task in filtered_tasks_by_type:
                print_project(task)
        else:
            print(Fore.RED + "No tasks found for this type." + Style.RESET_ALL)
    
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number between 1 and 4." + Style.RESET_ALL)
    
    # Display options for category filtering
    print(Fore.YELLOW + "\nSelect category to filter by:" + Style.RESET_ALL)
    print("[1] Academics")
    print("[2] Health")
    print("[3] Passion")
    print("[4] Career")
    print("[5] Entertainment")
    
    try:
        category_choice = int(input("Enter the number for category: "))
        filtered_tasks_by_category = filter_tasks_by_category(category_choice)
        
        if filtered_tasks_by_category:
            print(Fore.GREEN + Style.BRIGHT + "\nFiltered Tasks by Category:" + Style.RESET_ALL)
            for task in filtered_tasks_by_category:
                print_project(task)
        else:
            print(Fore.RED + "No tasks found for this category." + Style.RESET_ALL)
    
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number between 1 and 4." + Style.RESET_ALL)


def view_motto_desire_ui():
    print("\n--- View Motto/Desire ---")

    from db import filter_tasks_by_type
    tasks = filter_tasks_by_type(4)

    if not tasks:
        print("No Motto/Desire tasks found.\n")
        return

    for task in tasks:
        print_motto(task)
    print()
    
def view_task_description():
    task_id = int(input("Enter Task ID: "))
    from db import get_task_by_id
    task = get_task_by_id(task_id)
    
    if task:
        print(f"\nTitle: {task[1]}")
        print(f"Type: {task[2]}")
        print(f"Category: {task[3]}")
        print(f"\nDescription: \n{task[4]}\n")
        print(f"Status: {task[5]}")
        print(f"Assigned: {task[6]}")
        print(f"Start Date: {task[7]}")
        print(f"End Date: {task[8]}")
    else:
        print("Task not found.")

