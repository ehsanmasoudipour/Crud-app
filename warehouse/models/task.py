from django.db import models
from django.utils.translation import gettext_lazy as _
from warehouse.mixins import TimestampMixin

class Task(TimestampMixin):
    description = models.TextField(
        _("Description"),
        help_text=("Long Description.")
    )
    
    title = models.CharField(
        _("title"),
        unique = True,
        max_length = 100,
        help_text = _("title for tasks")
    )
    
    class meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")
    
    def __str__(self) -> str:
            return self.title
    
    def __repr__(self) -> str:
        return self.title