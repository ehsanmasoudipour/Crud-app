
from django.db.models import QuerySet


class TaskDataAccessQuerySet(QuerySet):
    def read_tasks(self, title = True):
        read_task = self.get(title = title)
        return read_task
        
    def delete_tasks(self, title = True):
        delete_tasks = self.delete(title = title)
        return delete_tasks
    
    def update_tasks(self, title = True):
        update_tasks = self.update(title = title)
        return update_tasks
    
    def create(self, title =True):
        create_tasks = self.create(title = title)
        return create_tasks