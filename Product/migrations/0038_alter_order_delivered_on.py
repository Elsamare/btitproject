# Generated by Django 4.2.6 on 2023-12-03 14:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0037_alter_order_delivered_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivered_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 3, 15, 9, 17, 390544, tzinfo=datetime.timezone.utc)),
        ),
    ]
