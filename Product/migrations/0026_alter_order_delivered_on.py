# Generated by Django 4.2.6 on 2023-11-27 17:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0025_alter_order_delivered_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivered_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 18, 10, 10, 78622, tzinfo=datetime.timezone.utc)),
        ),
    ]
