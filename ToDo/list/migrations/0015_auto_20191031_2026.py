# Generated by Django 2.2.6 on 2019-10-31 14:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0014_auto_20191031_2006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table_todo',
            old_name='Title',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='table_todo',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2019, 10, 31, 14, 56, 8, 513826, tzinfo=utc)),
        ),
    ]
