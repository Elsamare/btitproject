# Generated by Django 4.2.6 on 2023-11-26 06:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0012_alter_order_delivered_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivered_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 26, 6, 38, 10, 840401, tzinfo=datetime.timezone.utc)),
        ),
    ]
