# Generated by Django 2.2.6 on 2019-10-31 13:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0009_auto_20191031_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table_todo',
            name='date',
        ),
        migrations.AddField(
            model_name='table_todo',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2019, 10, 31, 13, 20, 0, 63038, tzinfo=utc)),
        ),
    ]
