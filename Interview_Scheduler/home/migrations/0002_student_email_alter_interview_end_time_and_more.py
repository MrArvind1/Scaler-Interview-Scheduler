# Generated by Django 4.1.1 on 2022-09-25 14:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='interview',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 25, 14, 25, 1, 401072)),
        ),
        migrations.AlterField(
            model_name='interview',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 25, 14, 25, 1, 401061)),
        ),
    ]
