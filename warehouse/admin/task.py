from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from warehouse.models.task import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created",
        "modified"
    )
    save_on_top =True
    
    search_fields = ("title",)
    
    search_filter = (
        "created",
        "modified",
        )