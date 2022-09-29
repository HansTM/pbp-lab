from django.db import models

class BarangWishlist(models.Model):
	nama_barang = models.CharField(max_length=50)
	harga_barang = models.IntegerField()
	deskripsi = models.TextField()

	def __str__(self) -> str:
		return self.nama_barang