class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            status = "Completed" if task.completed else "Pending"
            print(f"{i}. {task.title} - {status}")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
        else:
            print("Invalid task index")

# Create a sample To-Do List
todo_list = ToDoList()

while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Quit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        task = Task(title, description)
        todo_list.add_task(task)
        print("Task added!")

    elif choice == "2":
        print("\nTasks:")
        todo_list.view_tasks()

    elif choice == "3":
        task_index = int(input("Enter task index to mark as completed: ")) - 1
        todo_list.mark_task_completed(task_index)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")
