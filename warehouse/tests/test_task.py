from django.test import TestCase

from warehouse.models.task import Task
from warehouse.repository.generator import TaskDGL


class TestTaskModel(TestCase):
    def setUp(self):
        DGL = TaskDGL()
        self.TOTAL_TASKS = 20
        self.tasks = DGL.create_tasks(self.TOTAL_TASKS)

    def test_str_method(self):
        for i in range(self.TOTAL_TASKS):
            task = self.tasks[i]
            actual = str(task)
            expected = task.title
            self.assertEqual(
                actual,
                expected,
                msg = f"we expected `{expected}` but actual is `{actual}`"
                )   
            
    def test_verbose_name(self):
        self.assertEqual(Task.meta.verbose_name, "Task")
        self.assertEqual(Task.meta.verbose_name_plural, "Tasks")
