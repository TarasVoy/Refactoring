# refactored_code.py

from typing import List

class Task:
    def __init__(self, name: str, priority: str):
        self.name = name
        self.priority = priority
        self.done = False

    def complete(self):
        self.done = True

    def __str__(self):
        status = "✔" if self.done else "✘"
        return f"{self.name} [{self.priority}] {status}"

class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, name: str, priority: str):
        self.tasks.append(Task(name, priority))

    def complete_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index].complete()

    def list_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")
