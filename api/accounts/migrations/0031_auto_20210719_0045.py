# Generated by Django 2.2.24 on 2021-07-18 19:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_auto_20210718_2313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attachment',
            old_name='name',
            new_name='email',
        ),
        migrations.AlterField(
            model_name='registry',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 19, 0, 45, 36, 510210)),
        ),
    ]
