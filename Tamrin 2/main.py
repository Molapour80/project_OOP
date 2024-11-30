##github.com/Molapour80/project_OOP
import datetime
from Task import Task
from Project import Project
from both import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\nOptions: add_project, remove_project, edit_project, add_task, remove_task, display_projects, display_tasks, exit")
        command = input("Enter a command: ").strip().lower()

        if command == "exit":
            print("Exiting the program.")
            break

        elif command == "add_project":
            project_name = input("Enter project name: ")
            manager.add_project(project_name)

        elif command == "remove_project":
            project_name = input("Enter project name to remove: ")
            manager.remove_project(project_name)

        elif command == "edit_project":
            old_name = input("Enter current project name: ")
            new_name = input("Enter new project name: ")
            manager.edit_project(old_name, new_name)

        elif command == "add_task":
            project_name = input("Enter project name: ")
            if project_name in manager.projects:
                task_id = input("Enter task ID: ")
                task_name = input("Enter task name: ")
                task_description = input("Enter task description: ")
                task = Task(id_=task_id, name=task_name, description=task_description)
                task.start_task()  
                manager.projects[project_name].add_task(task)
            else:
                print("Project not found.")

        elif command == "remove_task":
            project_name = input("Enter project name: ")
            if project_name in manager.projects:
                task_id = input("Enter task ID to remove: ")
                result = manager.projects[project_name].remove_task(task_id)
                print(result)
            else:
                print("Project not found.")

        elif command == "display_projects":
            manager.display_projects()

        elif command == "display_tasks":
            project_name = input("Enter project name: ")
            if project_name in manager.projects:
                manager.projects[project_name].display_tasks()
            else:
                print("Project not found.")

        else:
            print("Invalid command. Please try again.")


main()