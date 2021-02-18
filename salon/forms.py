from django import forms
from salon.models import *

class TambahBarangForm(forms.ModelForm):
    class Meta: 
        model = Barang
        fields = '__all__'

        def __init__(self, *args, **kwargs):  
            super(TambahBarangForm, self).__init__(*args, **kwargs)

            for visible in self.visible.fields():
                visible.field.widget.attrs['class'] = 'form-control input-sm'

 
class TambahTransaksiForm(forms.ModelForm):
    class Meta:
        model  = Transaksi
        fields = '__all__'

        def __init__(self, *args, **kwargs):  
            super(TambahTransaksiForm, self).__init__(*args, **kwargs)
            for visible in self.visible.fields():
                visible.field.widget.attrs['class'] = 'form-control input-sm'  