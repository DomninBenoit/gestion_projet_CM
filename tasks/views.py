from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from tasks.models import Task
from tasks.serializer import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
