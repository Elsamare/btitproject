# Generated by Django 4.2.6 on 2023-11-26 04:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivered_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 26, 5, 29, 26, 342527, tzinfo=datetime.timezone.utc)),
        ),
    ]
