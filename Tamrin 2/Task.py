import datetime

class Task:
    def __init__(self, id_, name, description):
        self.task_id = id_
        self.name = name
        self.description = description
        self.status = False
        self.start_time = None
        self.end_time = None

    def start_task(self):
        if self.start_time is None:
            self.start_time = datetime.datetime.now()
            return f"Task '{self.name}' started at {self.start_time}."
        return f"Task '{self.name}' is already started."

    def end_task(self):
        if self.start_time is not None and self.end_time is None:
            self.end_time = datetime.datetime.now()
            self.status = True
            return f"Task '{self.name}' ended at {self.end_time}. Time spent: {self.get_timespan()} hours."
        return f"Task '{self.name}' has not started yet."

    def mark_as_done(self):
        self.status = True
        print(f"Task '{self.name}' marked as done.")

    def edit_task(self, name=None, description=None):
        if name:
            self.name = name
        if description:
            self.description = description
        print(f"Task {self.task_id} updated: Name: {self.name}, Description: {self.description}.")

    def get_timespan(self):
        if self.start_time and self.end_time:
            span = self.end_time - self.start_time
            return span.total_seconds() / 3600
        return 0

    def __str__(self):
        return f"ID: {self.task_id}, Name: {self.name}, Description: {self.description}"