from tqdm import tqdm
from warehouse.models import (Task)
from painless.repository.generator import BaseDataGenerator


class TaskDataGeneratorLayer(BaseDataGenerator):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

    def create_tasks(self, total):
        objs = [
            Task(
                description=f"Task-{self.get_random_sentence(3)}",
                title=f"Task-{self.get_random_words(2)}",
                )
            for i in tqdm(range(total))
        ]

        tasks = Task.objects.bulk_create(
            objs,
            batch_size=10000
        )
        return tasks