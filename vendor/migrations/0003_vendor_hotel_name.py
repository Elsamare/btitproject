# Generated by Django 4.2.6 on 2023-11-17 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_vendor_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='hotel_name',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
