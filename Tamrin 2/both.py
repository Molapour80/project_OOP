from Project import Project

class TaskManager:
    def __init__(self):
        self.projects = {}

    def add_project(self, project_name):
        if project_name not in self.projects:
            self.projects[project_name] = Project(project_name)
            print(f"Project '{project_name}' added.")
        else:
            print("Project name must be unique.")

    def remove_project(self, project_name):
        if project_name in self.projects:
            del self.projects[project_name]
            print(f"Project '{project_name}' removed.")
        else:
            print("Project not found.")

    def edit_project(self, old_name, new_name):
        if old_name in self.projects:
            if new_name in self.projects:
                print("New project name must be unique.")
            else:
                self.projects[new_name] = self.projects.pop(old_name)
                self.projects[new_name].project_name = new_name
                print(f"Project '{old_name}' renamed to '{new_name}'.")
        else:
            print("Project not found.")

    def display_projects(self):
        for project_name, project in self.projects.items():
            print(f"Project: {project_name}, Number of Tasks: {len(project)} ")

    def search_project(self, project_name):
        return self.projects.get(project_name)