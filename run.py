import json


tasks = []

def show_options():
    print("ToDo List")
    print("1.Add a task")
    print("2.View tasks")
    print("3.Remove tasks")

def add_task(task):
    tasks.append(task)
    print(f"Task Added: {task}")
    print(f"your tasks are: {tasks}")


def main():
    while True:
        show_options()
        choose_option = input("Choose an option: ")
        if choose_option == '1':
            task = input("Enter your task: ")
            add_task(task)
        
    

main()