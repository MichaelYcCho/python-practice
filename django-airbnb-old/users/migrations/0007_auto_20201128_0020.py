# Generated by Django 2.2.5 on 2020-11-27 15:20

import core.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200411_0134'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', core.managers.CustomUserManager()),
            ],
        ),
    ]
