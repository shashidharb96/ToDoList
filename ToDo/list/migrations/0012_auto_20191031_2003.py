# Generated by Django 2.2.6 on 2019-10-31 14:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('list', '0011_auto_20191031_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='table_todo',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='table_todo',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2019, 10, 31, 14, 33, 40, 806122, tzinfo=utc)),
        ),
    ]
