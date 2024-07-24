import json
import os
import re

tasks = []
filename = "tasks.json"

def show_options():
    print("Choose a menu option to manage your To Do List")
    print("\n")
    print("1.Add a task")
    print("2.View tasks")
    print("3.Remove tasks")
    print("4.Mark Tasks Complete")
    print("")
    print('\n')

def add_task():
    while True:
        clear_screen()
        print('Add New Tasks')
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
            print('Add New Tasks')
            print("Press 'm' to return to main menu\n")  
            print(f"Task added: {task_des}\n")         
            due_date = input('\nEnter due date (YYYY-MM-DD): \n')
            date_pattern = (r'^\d{4}-\d{2}-\d{2}$')   
            if re.match(date_pattern, due_date):
                try:
                    year, month, day = map(int, due_date.split('-'))
                    break
                except ValueError:
                    print("\nInvalid date format. Please enter the date in YYYY-MM-DD format.")
            else:
                print('\nInvalid date format. Please enter the date in YYYY-MM-DD format.')
            input('Press Enter to try again.')
            clear_screen()  

            if task_des == "":
                continue

        while True:
            clear_screen()
            print('Add New Tasks')
            print("Press 'm' to return to main menu\n")  
            print(f"Task added: {task_des}")
            print(f"Due Date: {due_date}\n")
            priority = input('\nEnter priority level (low, medium, high): \n').strip().lower()
            if priority in ['low', 'medium', 'high']:
                break
            print("\nInvalid priority level. Please type, 'low', 'medium', 'high'")
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
        print("ADD NEW TASKS")
        print("Press 'm' to return to main menu\n")
        print("Adding task to list...\n")
        print(f"New task Added: {task['Task']}, \nDue Date: {task['Due Date']}, \nPriority: {task['Priority']}\n")

        user_input = input("Press Enter to continue \n")
        if user_input.lower() == 'm':
            clear_screen()
            break


def view_tasks():
    clear_screen()
    print('View your tasks')
    print("Press 'm to return to main menu\n")

    if not tasks:
        print("You have no current tasks.")
    else:
        print("Your current tasks are: ")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}.  Task: {task['Task']}, Due Date: {task['Due Date']}, Priority: {task['Priority']}")

    while True:
        user_input = input("\n").strip().lower()
        if user_input == 'm':
            clear_screen()
            break

def remove_tasks():
    while True:
        clear_screen()
        print('Remove Tasks')
        print("Press 'm to return to main menu\n")

        if not tasks:
            print("You have no current tasks.")
            user_input = input("\n").strip().lower()
            if user_input == 'm':
                clear_screen()
                break
        else:
            print("Your current tasks: ")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}.  Task: {task['Task']}, Due Date: {task['Due Date']}, Priority: {task['Priority']}")
                
            task_number = input('\nEnter task you want to remove from To Do List\n')
                
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
                    print(f"Task Removed: Task: {removed_task['Task']}, Due Date: {removed_task['Due Date']}, Priority: {removed_task['Priority']}\n")
                    input("Press Enter to continue\n")
                else:
                    print("\nInvalid task number")
                    input("Press Enter to try again.")         
            except ValueError:
                print("\nPlease enter a valid task number.")
                input("Press Enter to try again.")

def save_tasks():
    with open(filename, 'w') as file:
        json.dump(tasks, file)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_tasks():
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def mark_task_complete():
    clear_screen()
    while True:
        print('Mark your completed tasks')
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
                print(f"{idx}.  Task: {task['Task']}, Due Date: {task['Due Date']}, Priority: {task['Priority']}, Status: {status}") 

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


def main():
    global tasks
    tasks = load_tasks()
    while True:
        print("\n")
        print("Welcome to your ToDo List")
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