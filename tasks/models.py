from django.db import models
from users.models import User

list_status = [
    ('non_attribuee', 'Non attribuée'),
    ('attribuee', 'Attribuée'),
    ('en_cours', 'En cours'),
    ('cloturee', 'Cloturée'),
]


class Task(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField
    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)
    user_assigned = models.ManyToManyField(User, related_name="task", null=True)


class Task_dependencies(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    dependent_task_id = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="dependent_task")
