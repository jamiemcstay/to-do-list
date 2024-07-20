import json
import os

tasks = []
filename = "tasks.json"

def show_options():
    print("ToDo List")
    print("1.Add a task")
    print("2.View tasks")
    print("3.Remove tasks")

def add_task(task):
    print("Adding task to list...")
    tasks.append(task)
    save_tasks()
    print(f"New task Added: {task}")
    clear_screen()

def view_tasks():
    if not tasks:
        print("You have no current tasks.")
    else:
        print("Your current tasks: ")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

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


def main():
    while True:
        show_options()
        choose_option = input("Choose an option: \n")
        clear_screen()
        if choose_option == '1':
            task = input("Enter your task: \n")
            add_task(task)
        if choose_option == '2':
            view_tasks()
        if choose_option == '3':
            view_tasks()
            task_number = int(input('Enter task number to remove: \n'))
            remove_tasks(task_number)

main()