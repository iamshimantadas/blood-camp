# Generated by Django 5.0.1 on 2024-01-08 17:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_blooddonation'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orderdate',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
    ]