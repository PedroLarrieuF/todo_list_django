# Generated by Django 4.0.1 on 2022-02-15 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0003_typeoftask'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasks',
            options={'ordering': ['task_done'], 'verbose_name': 'Tarefas'},
        ),
        migrations.DeleteModel(
            name='TypeOfTask',
        ),
    ]
