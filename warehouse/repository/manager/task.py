from django.db.models import Manager
from warehouse.repository.queryset.task import TaskDataAccessQuerySet


class TaskDataAccessLayerManager(Manager):
    def get_queryset(self):
        return TaskDataAccessQuerySet(self.model, using=self._db)
    
    def read_tasks(self, title: str,):
        '''read a task with title '''
        return self.get_queryset().read_tasks(title)
    
    def delete_tasks(self, title: str,):
        '''delete a task with title '''
        return self.get_queryset().delete_tasks(title)   
    
    def update_tasks(self, title: str,):
        '''update a task with title '''
        return self.get_queryset().update_tasks(title) 
    
    def create_tasks(self, title: str,):
        '''create a task with title '''
        return self.get_queryset().create_tasks(title)