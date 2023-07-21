from rest_framework import serializers
from warehouse.models import Task
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
        ]
