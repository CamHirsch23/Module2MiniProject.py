def add_task(tasks):
    title = input("Enter the title of the task: ")
    tasks.append({"title": title, "status": "Incomplete"})
    print("Task added!")

def view_tasks(tasks):
    if tasks:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['title']} - {task['status']}")
    else:
        print("No tasks to display.")

def mark_task_complete(tasks):
    if tasks:
        task_number = int(input("Enter task number to mark as complete: "))
        if 0 < task_number <= len(tasks):
            tasks[task_number - 1]['status'] = "Complete"
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    else:
        print("No tasks available to mark as complete.")

def delete_task(tasks):
    if tasks:
        task_number = int(input("Enter task number to delete: "))
        if 0 < task_number <= len(tasks):
            del tasks[task_number - 1]
            print("Task deleted!")
        else:
            print("Invalid task number.")
    else:
        print("No tasks available to delete.")

def main():
    tasks = []
    while True:
        print("\nWelcome to the To-Do List App!\n")
        print("Menu:\n1. Add a task\n2. View tasks\n3. Mark a task as complete\n4. Delete a task\n5. Quit")
        choice = input("Choose an option: ")
        try:
            if choice == "1":
                add_task(tasks)
            elif choice == "2":
                view_tasks(tasks)
            elif choice == "3":
                mark_task_complete(tasks)
            elif choice == "4":
                delete_task(tasks)
            elif choice == "5":
                print("Thank you for using the To-Do List App!")
                break
            else:
                print("Invalid choice, please choose a valid option from 1 to 5.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nApplication closed by user.")
    finally:
        print("Application is closing...")
