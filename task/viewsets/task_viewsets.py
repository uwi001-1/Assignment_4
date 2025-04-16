from rest_framework import viewsets
from ..models import Task
from ..serializers.task_serializers import TaskListSerializers, TaskRetrieveSerializers, TaskWriteSerializers

from task.utilities.pagination import MyPageNumberPagination

class taskViewsets(viewsets.ModelViewSet):
    serializer_class = TaskListSerializers
    queryset = Task.objects.all().order_by('-id')
    pagination_class = MyPageNumberPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return TaskWriteSerializers
        elif self.action == 'retrieve':
            return TaskRetrieveSerializers
        return super().get_serializer_class()