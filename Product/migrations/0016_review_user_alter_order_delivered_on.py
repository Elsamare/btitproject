# Generated by Django 4.2.6 on 2023-11-26 06:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Product', '0015_remove_review_user_alter_order_delivered_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivered_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 26, 6, 49, 57, 4912, tzinfo=datetime.timezone.utc)),
        ),
    ]
