# Generated by Django 2.0.6 on 2018-07-11 17:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20180711_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop_item',
            name='product_url',
            field=models.CharField(default=uuid.UUID('c1dbfe81-9d32-4c80-bf8c-5d3ce41ced91'), max_length=100),
        ),
    ]
