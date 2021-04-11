from django.urls import path
from salon.views import *

urlpatterns = [
    path('', home, name='home'),
    path('barang/', barang, name='barang'),
    path('trans/', transaksi, name='trans'),
    path('tambah_trans/', tambah_transaksi, name='tambah-transaksi'),


]