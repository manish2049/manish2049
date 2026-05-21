def add_task():
    task = input("Enter task: ")

    with open("tasks.txt", "a") as f:
        f.write(task + "\n")

    print("Task added!")


def view_tasks():
    print("\nTasks:")

    with open("tasks.txt", "r") as f:
        tasks = f.readlines()

        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")


while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        break

    else:
        print("Invalid choice")
