# Generated by Django 2.2.24 on 2021-07-30 13:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0052_auto_20210730_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 30, 19, 22, 54, 420121)),
        ),
        migrations.AlterField(
            model_name='registry',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 30, 19, 22, 54, 420121)),
        ),
        migrations.AlterField(
            model_name='save_mail',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 30, 19, 22, 54, 420121)),
        ),
    ]
