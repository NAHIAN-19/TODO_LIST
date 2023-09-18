# Generated by Django 4.2 on 2023-06-13 18:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_List_App', '0037_alter_task_createddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='default.jpg', upload_to='profile_pictures'),
        ),
        migrations.AlterField(
            model_name='task',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 13, 18, 12, 8, 442794, tzinfo=datetime.timezone.utc)),
        ),
    ]
