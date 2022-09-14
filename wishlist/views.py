from django.shortcuts import render
from wishlist.models import BarangWishlist
from django.http import HttpResponse
from django.core import serializers

def show_wishlist(request):

    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Bapak H'
    }

    return render(request, "wishlist.html", context)

def show_wishlist_xml(request):

    data = BarangWishlist.objects.all()

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_wishlist_json(request):

    data = BarangWishlist.objects.all()

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_item_by_id_xml(request, id):

    data = BarangWishlist.objects.filter(pk=id)

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_item_by_id_json(request, id):

    data = BarangWishlist.objects.filter(pk=id)

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
