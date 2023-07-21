from rest_framework import serializers, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from warehouse.models import Task
from ..serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    allowed_methods = ['GET', 'PUT', 'POST', 'DELETE']
    lookup_field = 'title'
    lookup_url_kwarg = 'title'


class TaskAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task)
        else:
            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = TaskSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        task = Task.objects.get(pk=pk)
        data = TaskSerializer(task, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        task = Task.objects.get(pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)