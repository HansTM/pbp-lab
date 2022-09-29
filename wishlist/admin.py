from django.contrib import admin
from .models import BarangWishlist

class BarangWishlistAdmin(admin.ModelAdmin):
	list_display = ['pk', 'nama_barang']
	list_display_links = ['pk', 'nama_barang']
	ordering = ['pk']
admin.site.register(BarangWishlist, BarangWishlistAdmin)
