import json
import os

tasks = []
filename = "tasks.json"

def show_options():
    print("Please choose weather to add, view, or remove completed tasks")
    print("\n")
    print("1.Add a task")
    print("2.View tasks")
    print("3.Remove tasks")
    print("")
    print('\n')

def add_task():
    while True:
        clear_screen()
        print("Press 'm' to return to main menu\n")

        task_des = input("Add new task: \n")

        if task_des.lower() == 'm':
            break


        if task_des == "":
            continue


        due_date = input('\nEnter due date (YYYY-MM-DD): \n')
        priority = input('\nEnter priority level (low, medium, high): \n')

        task = {
            "Task": task_des,
            "Due Date": due_date,
            "Priority": priority
        }

        tasks.append(task)
        save_tasks()

        clear_screen()
        print("Press 'm' to return to main menu\n")
        print("Adding task to list...\n")
        print(f"New task Added: \nTask: {task['Task']}, \nDue Date: {task['Due Date']}, \nPriority: {task['Priority']}\n")

        user_input = input("Press Enter to add another task \n")
        if user_input.lower() == 'm':
            break


def view_tasks():
    clear_screen()
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
            break

def remove_tasks():
    while True:
        clear_screen()
        if not tasks:
            print("You have no current tasks.")
        else:
            print("Your current tasks: ")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")
        task_number = input('Enter completed task number to remove from list(or press Enter to return to main menu...)\n')
        if task_number == "":
            break
        try:
            task_number = int(task_number)
            if 0 < task_number <= len(tasks):
                removed_task = tasks.pop(task_number -1)
                save_tasks()
                print("Removing task..")
                print(f"Removed task: {removed_task}")
            else:
                print("Invalid task number")
        except ValueError:
            print("Please enter a valid number.")
        input("\nPress Enter to continue...")

def save_tasks():
    with open(filename, 'w') as file:
        json.dump({'Tasks': tasks}, file)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# def return_to_options():
#     input("\nPress Enter to return to main menu...")
#     clear_screen()
#     show_options()


def main():
    while True:
        clear_screen()
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
        else:
            print("Invalid menu option. Please choose again.")

main()