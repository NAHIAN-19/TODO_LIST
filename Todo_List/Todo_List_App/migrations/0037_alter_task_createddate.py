# Generated by Django 4.2 on 2023-06-13 15:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_List_App', '0036_alter_task_createddate_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 13, 15, 55, 51, 492142, tzinfo=datetime.timezone.utc)),
        ),
    ]
