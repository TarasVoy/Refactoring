# original_code.py

tasks = []

def add_task(name, priority):
    task = {
        "name": name,
        "priority": priority,
        "done": False
    }
    tasks.append(task)

def complete_task(index):
    if index < len(tasks):
        tasks[index]["done"] = True

def list_tasks():
    for i in range(len(tasks)):
        task = tasks[i]
        status = "✔" if task["done"] else "✘"
        print(f"{i + 1}. {task['name']} [{task['priority']}] {status}")
