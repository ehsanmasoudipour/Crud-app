from django.core.management.base import BaseCommand
from warehouse.repository.generator import TaskDGL

class Command(BaseCommand):
    def add_argument(self, parser) -> None:
        parser.add_argument('task_total', type=str, default = 1)

    def handle(self, *args, **options):
        task_total = int(options.get('tag_total', 10))
        DGL = TaskDGL()
        
        tags = DGL.create_tasks(task_total)
        print("tag Created.")