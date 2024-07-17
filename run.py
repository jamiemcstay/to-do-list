import json

tasks = []
filename = "tasks.json"

def show_options():
    print("ToDo List")
    print("1.Add a task")
    print("2.View tasks")
    print("3.Remove tasks")

def add_task(task):
    print("Adding task to list")
    tasks.append(task)
    print(f"New task Added: {task}")
    print(f"Your tasks are: {tasks}")

def view_tasks():
    if not tasks:
        print("You have no current tasks.")
    else:
        print("Your current tasks: ")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")


def main():
    while True:
        show_options()
        choose_option = input("Choose an option: ")
        if choose_option == '1':
            task = input("Enter your task: ")
            add_task(task)
        if choose_option == '2':
            view_tasks()
        if choose_option == '3':
            view_tasks()
            task_number = int(input('Enter task number to remove: '))
            remove_task()

main()