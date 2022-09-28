from django.test import TestCase, Client
from django.urls import resolve
from django.contrib.auth.models import User

class ViewsTest(TestCase):
	# def test_ok_index(self):
	# 	response = Client().get('/wishlist')
	# 	self.assertEqual(response.status_code, 200)

	# def test_template_index(self):
	# 	response = Client().get('/wishlist')
	# 	self.assertTemplateUsed(response, 'watchlist.html')

	def test_ok_json(self):
		response = Client().get('/wishlist/json/')
		self.assertEqual(response.status_code, 200)

	def test_ok_xml(self):
		response = Client().get('/wishlist/xml/')
		self.assertEqual(response.status_code, 200)

	def test_ok_login(self):
		response = Client().get('/wishlist/login/')
		self.assertEqual(response.status_code, 200)

	def test_template_login(self):
		response = Client().get('/wishlist/login/')
		self.assertTemplateUsed(response, 'login.html')

	def test_ok_register(self):
		response = Client().get('/wishlist/register/')
		self.assertEqual(response.status_code, 200)

	def test_template_register(self):
		response = Client().get('/wishlist/register/')
		self.assertTemplateUsed(response, 'register.html')

class ViewsLoggedInTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.client.force_login(User.objects.get_or_create(username='testuser')[0])

	def test_ok_index(self):
		response = self.client.get('/wishlist/')
		print(response)
		self.assertEqual(response.status_code, 200)