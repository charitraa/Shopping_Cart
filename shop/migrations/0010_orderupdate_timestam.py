# Generated by Django 4.2.5 on 2023-10-04 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_remove_orderupdate_city_remove_orderupdate_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderupdate',
            name='timestam',
            field=models.DateField(auto_now=True),
        ),
    ]
