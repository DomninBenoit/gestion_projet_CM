# Generated by Django 5.0.4 on 2024-05-02 12:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField(blank=True, null=True)),
                ('user_assigned', models.ManyToManyField(related_name='task', to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='Task_dependencies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dependent_task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dependent_task', to='tasks.task')),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
        ),
    ]
