# Generated by Django 4.0.1 on 2022-02-14 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='descr',
            new_name='description',
        ),
    ]
