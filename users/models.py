from django.db import models
from django.contrib.auth.hashers import make_password


list_fonctions = [
    ('maire', 'Maire'),
    ('adjoint', 'Adjoint'),
    ('conseiller', 'Conseiller'),
    ('employe', 'Employé'),
]


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    fonction = models.CharField(max_length=20, choices=list_fonctions)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)
