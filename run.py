import json
import os
import re

tasks = []
filename = "tasks.json"


def save_tasks():
    """
    Saves the current list of tasks to a json file.
    """
    with open(filename, 'w') as file:
        json.dump(tasks, file)


def clear_screen():

    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def load_tasks():
    """
    Loads taks from the json file into the task list.
    Returns list of tasks from the json file is they exist, and an empty list
    if file doesnt exist.
    """
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []


def show_options():
    """
    Displays the menu options for managing the To Do List.
    """
    print("Choose a menu option to manage your To Do List")
    print("\n")
    print("1.Add a task")
    print("2.View tasks")
    print("3.Remove tasks")
    print("4.Mark Tasks Complete")
    print("")
    print('\n')


def add_task():
    """
    Prompts the user to add a new task, including description , due date,
    and priority. Ensures the due date is in the YYYY-MM-DD format and
    the priority is the correct string.
    """
    while True:
        clear_screen()
        print_heading("TO DO LIST")
        print("\nADD NEW TASKS\n")
        print("Press 'm' to return to main menu\n")

        task_des = input("Add new task: \n")

        if task_des.lower() == 'm':
            clear_screen()
            break

        if not task_des.strip():
            print('Task description cannot be empty')
            input('Press Enter to try again')
            continue

        while True:
            clear_screen()
            print_heading("TO DO LIST")
            print("\nADD NEW TASKS\n")
            print(f"Task added: {task_des}\n")

            due_date = input('\nEnter due date (YYYY-MM-DD): \n')
            date_pattern = (r'^\d{4}-\d{2}-\d{2}$')
            if re.match(date_pattern, due_date):
                try:
                    year, month, day = map(int, due_date.split('-'))
                    break
                except ValueError:
                    print("\nInvalid date format. Please enter the date in")
                    print("YYYY-MM-DD format.")
            else:
                print("\nInvalid date format. Please enter the date in")
                print("YYYY-MM-DD format.")
            input('Press Enter to try again.')
            clear_screen()

            if task_des == "":
                continue

        while True:
            clear_screen()
            print_heading('TO DO LIST')
            print("\nADD NEW TASKS\n")
            print(f"Task added: {task_des}")
            print(f"Due Date: {due_date}\n")
            priority = input('\nEnter priority level(low, medium, high):\n')\
                .strip().lower()
            if priority in ['low', 'medium', 'high']:
                break
            print("\nInvalid priority level. Please type, 'low', 'medium',")
            print("'high'")
            input("Press Enter to try again\n")

        task = {
            "Task": task_des,
            "Due Date": due_date,
            "Priority": priority,
            "Status": False
        }

        tasks.append(task)
        save_tasks()

        clear_screen()
        print_heading("TO DO LIST")
        print('\nADD NEW TASKS\n')
        print("Press 'm' to return to main menu\n")
        print("Adding task to list...\n")
        print(f"New task Added: {task['Task']}")
        print(f"Due Date: {task['Due Date']}")
        print(f"Priority: {task['Priority']}")

        user_input = input("\nPress Enter to continue \n")
        if user_input.lower() == 'm':
            clear_screen()
            break


def remove_tasks():
    """
    Prompts the user to enter number of task to remove from To Do list.
    """
    while True:
        clear_screen()
        print_heading("TO DO LIST")
        print('\nREMOVE TASKS\n')
        print("Press 'm to return to main menu\n")

        if not tasks:
            print("\nYou have no current tasks.")
            user_input = input("\n").strip().lower()
            if user_input == 'm':
                clear_screen()
                break
        else:
            print("\nYour current tasks: ")
            for idx, task in enumerate(tasks, 1):
                status = 'Complete' if task['Status'] else 'Incomplete'
                print(f"{idx}.Task: {task['Task']}")
                print(f"Due Date: {task['Due Date']}")
                print(f"Priority: {task['Priority']}")
                print(f"Status: {status}")

            task_number = input('\nEnter task number to remove from List')

            if task_number == 'm':
                clear_screen()
                break

            if task_number == "":
                continue

            try:
                task_number = int(task_number)
                if 0 < task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    save_tasks()
                    print("\nRemoving task..")
                    print(f"Task Removed: Task: {removed_task['Task']}")
                    print(f"Due Date: {removed_task['Due Date']}")
                    print(f"Priority: {removed_task['Priority']}")
                    input("Press Enter to continue\n")
                else:
                    print("\nInvalid task number")
                    input("Press Enter to try again.")
            except ValueError:
                print("\nPlease enter a valid task number.")
                input("Press Enter to try again.")


def view_tasks():
    """
    Displays all tasks with their description, due date, priority level,\
    and status.
    """
    clear_screen()
    print_heading("TO DO LIST")
    print("\nVIEW TAKS\n")
    print("Press 'm to return to main menu\n")

    if not tasks:
        print("You have no current tasks.")
    else:
        print("Your current tasks are: ")
        for idx, task in enumerate(tasks, 1):
            status = 'Complete' if task['Status'] else 'Incomplete'
            print(f"{idx}.Task: {task['Task']}")
            print(f"Due Date: {task['Due Date']}")
            print(f"Priority: {task['Priority']}")
            print(f"Status: {status}")

    while True:
        user_input = input("\n").strip().lower()
        if user_input == 'm':
            clear_screen()
            break


def mark_task_complete():
    """
    Prompts the user to mark a specific task as complete.
    Updates the task status to 'Complete' and saves updated tasks.
    """
    clear_screen()
    while True:
        print_heading("TO DO LIST")
        print("\nMARK COMPLETE TASKS\n")
        print("Press 'm' to return to main menu")

        if not tasks:
            print('\nYou have no current tasks.')
            user_input = input("\n").strip().lower()
            if user_input == 'm':
                clear_screen()
                break
        else:
            print('\nYour current tasks:')
            for idx, task in enumerate(tasks, 1):
                status = 'Complete' if task['Status'] else 'Incomplete'
                print(f"{idx}.Task: {task['Task']}")
                print(f"Due Date: {task['Due Date']}")
                print(f"Priority: {task['Priority']}")
                print(f"Status: {status}")

            task_number = input("\nEnter task number to mark as complete: \n")

            if task_number.lower() == 'm':
                clear_screen()
                break

            if task_number == "":
                continue

            try:
                task_number = int(task_number)
                if 0 < task_number <= len(tasks):
                    task = tasks[task_number - 1]
                    if task['Status']:
                        print("\nThis task is already complete...")
                        input('Press Enter to continue\n')
                        clear_screen()
                    else:
                        print("\nMarking task as complete...")
                        task['Status'] = True
                        save_tasks()
                        print(f"Task complete: {task['Task']}\n")
                        input('Press Enter to continue')
                        clear_screen()
                else:
                    print("\nInvalid task number")
                    input('Press Enter to try again\n')
                    clear_screen()

            except ValueError:
                print('\nPlease enter a valid number')
                input('Press Enter to try again.')
                clear_screen()


def print_heading(heading):

    ascii_art = {
        "TO DO LIST": r"""

  _______ ____    _____   ____    _      _____  _____ _______
 |__   __/ __ \  |  __ \ / __ \  | |    |_   _|/ ____|__   __|
    | | | |  | | | |  | | |  | | | |      | | | (___    | |
    | | | |  | | | |  | | |  | | | |      | |  \___ \   | |
    | | | |__| | | |__| | |__| | | |____ _| |_ ____) |  | |
    |_|  \____/  |_____/ \____/  |______|_____|_____/   |_|
    """
    }

    print(ascii_art.get(heading, heading))
    print("\n")


def main():
    """
    Main function to run the To Do List application.
    Displays main menu options, and handles user input to perform actions \
    within menu items.
    """
    global tasks
    tasks = load_tasks()
    while True:
        print("\n")
        print_heading("TO DO LIST")
        show_options()
        choose_option = input("Choose an option: \n")
        if choose_option == '1':
            clear_screen()
            add_task()
        elif choose_option == '2':
            view_tasks()
        elif choose_option == '3':
            remove_tasks()
        elif choose_option == '4':
            mark_task_complete()
        else:
            print("\nInvalid menu option.")
            user_input = input('Press enter to choose again\n')
            clear_screen()


main()
