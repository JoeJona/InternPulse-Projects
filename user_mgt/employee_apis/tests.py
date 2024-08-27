from django.test import TestCase
from django.urls import reverse, resolve
from . import views


# Create your tests here.


class TestUrls(TestCase):

    def test_create_employee(self):
        url = reverse('create_employee')
        self.assertEqual(resolve(url).func, views.create_employee)

    def test_get_employee_by_id(self):
        url = reverse('get_employee_by_id', kwargs={'eid': 1})
        self.assertEqual(resolve(url).func, views.employee_by_id)
