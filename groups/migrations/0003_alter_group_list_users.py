# Generated by Django 5.0.4 on 2024-05-07 09:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_alter_group_list_users'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='list_users',
            field=models.ManyToManyField(null=True, related_name='custom_group', to=settings.AUTH_USER_MODEL),
        ),
    ]
