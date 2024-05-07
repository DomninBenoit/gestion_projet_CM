from rest_framework.permissions import IsAuthenticated
from users.models import User
from rest_framework import viewsets
from users.serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]




