import os

FILE_NAME = "tasks.txt"


def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()
                if "|" in line:
                    status, task = line.split("|", 1)
                    tasks.append({"task": task, "done": status == "1"})
    return tasks


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            status = "1" if task["done"] else "0"
            file.write(f"{status}|{task['task']}\n")


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return

    print("\n------ TO-DO LIST ------")
    for i, task in enumerate(tasks, start=1):
        mark = "✓" if task["done"] else " "
        print(f"{i}. [{mark}] {task['task']}")
    print()


def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)
        print("Task added successfully.\n")


def complete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Task number to mark completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            save_tasks(tasks)
            print("Task marked as completed.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Deleted: {removed['task']}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def main():
    tasks = load_tasks()

    while True:
        print("====== TO-DO LIST ======")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()