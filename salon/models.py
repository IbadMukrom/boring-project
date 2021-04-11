from django.db import models

class Barang(models.Model):
    nama_barang = models.CharField(max_length=100, null=True, blank=True)
    jumlah      = models.IntegerField()
    harga       = models.DecimalField(decimal_places=2, max_digits=10)
    pemakaian   = models.IntegerField()
    
    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return self.nama_barang 


class JenisPerawatan(models.Model):
    nama_perawatan  = models.CharField(max_length=100)
    harga_perawatan = models.IntegerField()
    def __str__(self):
        return self.nama_perawatan
     
class Transaksi(models.Model):
    JENIS_KELAMIN = (
        ('LAKI-LAKI', 'LAKI-LAKI'),
        ('PEREMPUAN', 'PEREMPUAN'),
    )
    nama_pelanggan  = models.CharField(max_length=100, null=True, blank=True)
    Kelamin         = models.CharField(choices=JENIS_KELAMIN, max_length=100)
    tanggal         = models.DateTimeField(auto_now_add=True)
    pilih_perawatan = models.ForeignKey(JenisPerawatan, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-id']
        
    def __str__(self):
        return self.nama_pelanggan

