# Generated by Django 4.2 on 2023-06-12 14:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_List_App', '0025_remove_task_duetime_alter_task_createddate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 12, 14, 15, 11, 164020, tzinfo=datetime.timezone.utc)),
        ),
    ]
