# Generated by Django 3.2.5 on 2021-07-10 10:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_registry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registry',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 10, 15, 37, 0, 516639)),
        ),
    ]