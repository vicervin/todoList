# Generated by Django 2.0.2 on 2018-02-05 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180205_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
