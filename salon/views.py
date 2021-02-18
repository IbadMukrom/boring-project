from django.shortcuts import render, redirect
from django.views import View
from salon.forms import *
from salon.models import *
from django.db.models import Sum

def home(request):
    total = Barang.objects.count()
    uang_barang = Barang.objects.aggregate(Sum('harga'))['harga__sum']
    uang_transaksi = Transaksi.objects.aggregate(Sum('pilih_perawatan__harga_perawatan'))['pilih_perawatan__harga_perawatan__sum']
    total_transaksi = Transaksi.objects.all().count()
    data = {
        'uang_barang': uang_barang,
        'uang_transaksi': uang_transaksi,
        'total':total,
        'total_transaksi':total_transaksi,  
    }
    return render(request,'salon/home.html', data)

def barang(request):
    barang = Barang.objects.all()
    return render(request, 'salon/barang.html', {'barang':barang})

def transaksi(request):
    trans = Transaksi.objects.all()
    return render(request, 'salon/trans.html', {'trans':trans})

def tambah_transaksi(request):
    form = TambahTransaksiForm()
    if request.method=='POST':
        form = TambahTransaksiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trans')
    return render(request, 'salon/trans_form.html',{'form':form})