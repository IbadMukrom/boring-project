# Generated by Django 3.0 on 2021-02-17 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0004_auto_20210217_0139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaksi',
            old_name='jenis_perawatan',
            new_name='pilih_perawatan',
        ),
    ]
