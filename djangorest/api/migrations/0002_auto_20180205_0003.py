# Generated by Django 2.0.2 on 2018-02-05 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='checked',
            new_name='done',
        ),
    ]
