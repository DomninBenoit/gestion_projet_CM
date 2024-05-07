from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from groups.models import Group
from groups.serializer import GroupSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]
