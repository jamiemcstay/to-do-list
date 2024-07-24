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

            if task_des == "":
                continue

        while True:
            priority = input('\nEnter priority level (low, medium, high): \n').strip().lower()
            if priority in ['low', 'medium', 'high']:
                break
            print("\nInvalid priority level. Please type, 'low', 'medium', 'high'")
            input("Press Enter to try again\n")

        task = {
            "Task": task_des,
            "Due Date": due_date,
            "Priority": priority,
            "Completed": False
        }

        tasks.append(task)
        save_tasks()

        clear_screen()
        print("Press 'm' to return to main menu\n")
        print("Adding task to list...\n")
        print(f"New task Added: \nTask: {task['Task']}, \nDue Date: {task['Due Date']}, \nPriority: {task['Priority']}\n")

        user_input = input("Press Enter to add another task \n")
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
                break
        else:
            print("Your current tasks: ")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}.  Task: {task['Task']}, Due Date: {task['Due Date']}, Priority: {task['Priority']}")
                
            task_number = input('\nEnter task you want to remove from To Do List\n')
                
            if task_number == 'm':
                    break

            if task_number == "":
                    continue

            try:
                task_number = int(task_number)
                if 0 < task_number <= len(tasks):
                    removed_task = tasks.pop(task_number -1)
                    save_tasks()
                    clear_screen()
                    print("Press 'm' to return to main menu\n")
                    print("Removing task..")
                    print(f"Task Removed: Task: {removed_task['Task']}, Due Date: {removed_task['Due Date']}, Priority: {removed_task['Priority']}\n")
                else:
                    print("Invalid task number")
            except ValueError:
                print("Please enter a valid number.")

            input("Press Enter to continue\n")

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
    while True:
        clear_screen()
        print('Mark your completed tasks')
        print("Press 'm' to return to main menu")

        if not tasks:
            print('You have no current tasks.')
            user_input = input("\n").strip().lower()
            if user_input == 'm':
                break
        else:
            print('Your current tasks: ')
            for idx, task in enumerate(tasks, 1):
                status = 'Completed' if task.get('Completed') else 'Incomplete'
                print(f"{idx}.  Task: {task['Task']}, Due Date: {task['Due Date']}, Priority: {task['Priority']}") 

            task_number = input("\nEnter task number to mark as complete\n")

            if task_number.lower() == 'm':
                break

            if task_number == "":
                continue

            try:
                task_number = int(task_number)
                if 0 < task_number <= len(tasks):
                    task = tasks[task_number - 1]
                    print("Press 'm' to return to main menu\n")
                    print("Marking task as completed...")
                    task['Completed'] = True
                    save_tasks()
                    clear_screen()
                    print(f"Task marked as completed: Task: {task['Task']}")
                else:
                    print("Invalid task number")

            except ValueError:
                print('Please enter a valid number')


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