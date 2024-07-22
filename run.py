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
        task_des = input("Enter your task: \n")
        if task_des == "":
            break
        due_date = input('Enter due date (YYYY-MM-DD): \n')
        priority = input('Enter priority level (low, medium, high): \n')
        task = {
            "Description": task_des,
            "Due date": due_date,
            "Priority": priority
        }
        tasks.append(task)
        save_tasks()
        print("Adding task to list...")
        print(f"New task Added: {task}")
        if



def view_tasks():
    clear_screen()

    if not tasks:
        print("You have no current tasks.")
    else:
        print("Your current tasks are: ")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    input("\nPress Enter to return to main menu...")

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

def return_to_options():
    input("\nPress Enter to return to main menu...")
    clear_screen()
    show_options()


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
        if choose_option == '2':
            view_tasks()
        if choose_option == '3':
            remove_tasks()

main()