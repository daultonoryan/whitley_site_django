# Generated by Django 2.0.6 on 2018-07-09 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20180709_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop_item',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='shop_item',
            name='url',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
