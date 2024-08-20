from django.test import TestCase
from django.urls import reverse, resolve
from . import views


# Create your tests here.


class TestUrls(TestCase):

    def test_create_user(self):
        url = reverse('create_user')
        self.assertEqual(resolve(url).func, views.create_user)

    def test_get_user_by_id(self):
        url = reverse('get_user_by_id', kwargs={'uid': 1})
        self.assertEqual(resolve(url).func, views.user_by_id)

    def test_get_user_by_name(self):
        url = reverse('get_user_by_name')
        self.assertEqual(resolve(url).func, views.user_by_name)
