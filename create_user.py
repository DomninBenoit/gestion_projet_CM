import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_projet_CM.settings')

import django
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()


def create_test_user():
    username = 'conseiller'
    password = 'password123'
    email = 'conseiller@example.com'
    first_name = 'con'
    last_name = 'seiller'
    fonction = 'conseiller'
    phone = '1234567890'

    user = User.objects.create_user(
        username=username,
        password=password,
        email=email,
        first_name=first_name,
        last_name=last_name,
        fonction=fonction,
        phone=phone
    )

    print(f"Utilisateur {user.username} créé avec succès !")

create_test_user()
