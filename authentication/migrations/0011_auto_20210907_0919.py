# Generated by Django 3.2.4 on 2021-09-07 09:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_auto_20210831_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetinfo',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 8, 9, 19, 52, 621818, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=30),
        ),
    ]
