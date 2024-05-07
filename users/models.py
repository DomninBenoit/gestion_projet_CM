from django.db import models
from django.contrib.auth.models import AbstractUser


list_fonctions = [
    ('maire', 'Maire'),
    ('adjoint', 'Adjoint'),
    ('conseiller', 'Conseiller'),
    ('employe', 'Employé'),
]


class User(AbstractUser):
    fonction = models.CharField(max_length=20, choices=list_fonctions)
    phone = models.CharField(max_length=20, null=True)
    username = models.CharField(max_length=150, unique=True, default='')

