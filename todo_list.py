import json
from pathlib import Path

file = Path(__file__).with_name("tasks.json")


def load_tasks():
    if file.exists():
        try:
            with open(file, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    return []


def save_tasks(tasks):
    with open(file, "w") as f:
        json.dump(tasks, f, indent=4)


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\nTo-Do List")
    print("-" * 40)

    for task in tasks:
        status = "Done" if task["done"] else "Pending"
        print(f'{task["id"]}. {task["title"]} - {status}')
        if task["description"]:
            print(f'   {task["description"]}')

    print("-" * 40)


def add_task(tasks):
    title = input("Enter task title: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    description = input("Enter description: ").strip()

    new_id = 1
    if tasks:
        new_id = max(task["id"] for task in tasks) + 1

    tasks.append({
        "id": new_id,
        "title": title,
        "description": description,
        "done": False
    })

    save_tasks(tasks)
    print("Task added.")


def find_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def update_task(tasks):
    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    task = find_task(tasks, task_id)

    if not task:
        print("Task not found.")
        return

    title = input(f'Enter new title [{task["title"]}]: ').strip()
    description = input(
        f'Enter new description [{task["description"]}]: '
    ).strip()

    if title:
        task["title"] = title
    if description:
        task["description"] = description

    save_tasks(tasks)
    print("Task updated.")


def complete_task(tasks):
    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    task = find_task(tasks, task_id)

    if not task:
        print("Task not found.")
        return

    task["done"] = not task["done"]
    save_tasks(tasks)

    if task["done"]:
        print("Task marked as done.")
    else:
        print("Task marked as pending.")


def delete_task(tasks):
    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    task = find_task(tasks, task_id)

    if not task:
        print("Task not found.")
        return

    tasks.remove(task)
    save_tasks(tasks)
    print("Task deleted.")


def main():
    tasks = load_tasks()

    while True:
        print("""
========== TO-DO LIST ==========

1. Add task
2. View tasks
3. Update task
4. Mark task complete
5. Delete task
6. Exit
""")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
