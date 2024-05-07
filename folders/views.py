from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from folders.models import Folder
from folders.serializer import FolderSerializer


class FolderViewSet(ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [IsAuthenticated]
