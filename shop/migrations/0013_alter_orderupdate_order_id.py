# Generated by Django 4.2.5 on 2023-10-04 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_orderupdate_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='order_id',
            field=models.IntegerField(),
        ),
    ]
