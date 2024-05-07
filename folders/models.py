from django.db import models
from groups.models import Group


list_status = [
    ('non_attribue', 'Non attribué'),
    ('attribue', 'Attribué'),
    ('en_cours', 'En cours'),
    ('cloture', 'Cloturé'),
]


class Folder(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField
    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name="folder", null=True)
    status = models.CharField(max_length=20, choices=list_status)
