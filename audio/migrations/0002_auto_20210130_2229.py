# Generated by Django 3.1 on 2021-01-30 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='upload_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
