# Generated by Django 4.2.5 on 2023-10-08 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_delete_orderupdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('update_desc', models.CharField(default='', max_length=300)),
                ('timestamp', models.DateField(auto_now=True)),
            ],
        ),
    ]
