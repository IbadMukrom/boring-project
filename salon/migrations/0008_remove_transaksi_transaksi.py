# Generated by Django 3.0 on 2021-02-17 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0007_auto_20210217_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaksi',
            name='transaksi',
        ),
    ]