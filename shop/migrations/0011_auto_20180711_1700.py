# Generated by Django 2.0.6 on 2018-07-11 17:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20180711_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop_item',
            name='product_url',
            field=models.CharField(blank=True, default=uuid.UUID('9a291585-263b-43e1-a1b8-9eeb671e57ea'), max_length=100, unique=True),
        ),
    ]