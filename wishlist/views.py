from django.shortcuts import render
from wishlist.models import BarangWishlist

data_barang_wishlist = BarangWishlist.objects.all()
context = {
    'list_barang': data_barang_wishlist,
    'nama': 'Bapak H'
}

def show_wishlist(request):
    return render(request, "wishlist.html", context)