# Generated by Django 4.2.6 on 2023-12-04 05:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0044_alter_order_delivered_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivered_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 4, 6, 4, 2, 651285, tzinfo=datetime.timezone.utc)),
        ),
    ]
