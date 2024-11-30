from Task import Task
class Project:
    def __init__(self, project_name):
        self.project_name = project_name
        self.tasks = {}

    def add_task(self, task):
        if task.task_id not in self.tasks:
            self.tasks[task.task_id] = task
            print(f"Task '{task.name}' added to project '{self.project_name}'.")
        else:
            print(f"Task ID '{task.task_id}' already exists in project '{self.project_name}'.")

    def remove_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            return f"Task {task_id} removed from project {self.project_name}."
        return "Task ID not found."

    def display_tasks(self):
        print(f"Tasks in project '{self.project_name}':")
        if not self.tasks:
            print("No tasks found.")
        for task in self.tasks.values():
            print(f"- {task}")

    def __len__(self):
        return len(self.tasks)

    def get_project_name(self):
        return self.project_name