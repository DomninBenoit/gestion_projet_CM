# Generated by Django 5.0.4 on 2024-05-02 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('fonction', models.CharField(choices=[('maire', 'Maire'), ('adjoint', 'Adjoint'), ('conseiller', 'Conseiller'), ('employe', 'Employé')], max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
