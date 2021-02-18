# Generated by Django 3.0 on 2021-02-16 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_barang', models.CharField(blank=True, max_length=100, null=True)),
                ('jumlah', models.IntegerField()),
                ('harga', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pemakaian', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HargaPerawatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('harga', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='JenisPerawatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_perawatan', models.CharField(max_length=100)),
                ('harga_perawatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salon.HargaPerawatan')),
            ],
        ),
        migrations.CreateModel(
            name='Transaksi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pelanggan', models.CharField(blank=True, max_length=100, null=True)),
                ('Kelamin', models.CharField(choices=[('LAKI-LAKi', 'LAKI-LAKI'), ('PEREMPUAN', 'PEREMPUAN')], max_length=100)),
                ('tanggal', models.DateTimeField()),
                ('Transaksi', models.DecimalField(decimal_places=2, max_digits=10)),
                ('jenis_perawatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salon.JenisPerawatan')),
            ],
        ),
    ]