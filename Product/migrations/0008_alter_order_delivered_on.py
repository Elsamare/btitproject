# Generated by Django 4.2.6 on 2023-11-26 05:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0007_alter_order_delivered_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivered_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 26, 5, 55, 47, 133814, tzinfo=datetime.timezone.utc)),
        ),
    ]
