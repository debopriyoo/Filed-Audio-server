# Generated by Django 3.1 on 2021-01-31 14:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0006_auto_20210131_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobook',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 31, 14, 51, 30, 302936, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='participants',
            field=models.CharField(blank=True, default='', max_length=1100),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 31, 14, 51, 30, 302936, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='song',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 31, 14, 51, 30, 301940, tzinfo=utc)),
        ),
    ]
