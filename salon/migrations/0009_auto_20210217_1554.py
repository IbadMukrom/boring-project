# Generated by Django 3.0 on 2021-02-17 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0008_remove_transaksi_transaksi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaksi',
            name='tanggal',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]