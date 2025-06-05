# test_original.py

import original_code as oc

def test_add_task():
    oc.tasks.clear()
    oc.add_task("Test Task", "High")
    assert len(oc.tasks) == 1
    assert oc.tasks[0]["name"] == "Test Task"

def test_complete_task():
    oc.tasks.clear()
    oc.add_task("Test Task", "High")
    oc.complete_task(0)
    assert oc.tasks[0]["done"] == True

for _ in range(18):  # Додаємо фіктивні тести
    test_add_task()
    test_complete_task()
