# Generated by Django 2.0.6 on 2018-07-11 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20180709_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop_item',
            name='product_url',
            field=models.CharField(blank=True, default='<djangodbfieldsCharField>', max_length=100),
        ),
    ]
