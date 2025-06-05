# test_refactored.py

from refactored_code import TaskManager

def test_add_task():
    tm = TaskManager()
    tm.add_task("Test Task", "Low")
    assert len(tm.tasks) == 1
    assert tm.tasks[0].name == "Test Task"

def test_complete_task():
    tm = TaskManager()
    tm.add_task("Test Task", "Low")
    tm.complete_task(0)
    assert tm.tasks[0].done

for _ in range(18):
    test_add_task()
    test_complete_task()
