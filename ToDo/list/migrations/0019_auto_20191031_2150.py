# Generated by Django 2.2.6 on 2019-10-31 16:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0018_auto_20191031_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table_todo',
            name='author',
        ),
        migrations.AlterField(
            model_name='table_todo',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2019, 10, 31, 16, 20, 29, 897674, tzinfo=utc)),
        ),
    ]
