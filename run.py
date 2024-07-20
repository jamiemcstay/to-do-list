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
        task = input("Enter your task: (or press enter to return to main menu) \n")
        if task == "":
            break
        tasks.append(task)
        save_tasks()
        print("Adding task to list...")
        print(f"New task Added: {task}")



def view_tasks():
    clear_screen()

    if not tasks:
        print("You have no current tasks.")
    else:
        print("Your current tasks are: ")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    input("\nPress Enter to return to main menu...")

def remove_tasks(task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks()
        print(f"Removed task: {removed_task}")
    else:
        print("Invalid task number")

def save_tasks():
    with open(filename, 'w') as file:
        json.dump(tasks, file)

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
            view_tasks()
            task_number = int(input('Enter task number to remove: \n'))
            remove_tasks(task_number)

main()