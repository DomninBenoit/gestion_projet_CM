from django.db import models
from users.models import User


class Group(models.Model):
    name = models.CharField(max_length=100)
    list_users = models.ManyToManyField(User, related_name="group")
