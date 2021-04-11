from django.contrib import admin
from salon.models import *

# class TransaksiAdmin(admin.ModelAdmin):
    # list_display = ('nama_pelanggan', 'Kelamin' 'tanggal','pilih_perawatan')


 
admin.site.register(Barang)
admin.site.register(JenisPerawatan)
admin.site.register(Transaksi)
# admin.site.register(HargaPerawatan)
