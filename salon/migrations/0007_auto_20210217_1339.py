# Generated by Django 3.0 on 2021-02-17 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0006_auto_20210217_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jenisperawatan',
            name='harga_perawatan',
            field=models.IntegerField(),
        ),
    ]
