from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Medication, Order, Statement

class UtibuHealthTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_place_order_view(self):
        response = self.client.get(reverse('place_order'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'place_order.html')

    def test_order_history_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('order_history'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_history.html')

    def test_statement_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('statement'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statement.html')

    def test_api_medications_list_create(self):
        response = self.client.get(reverse('medication-list-create'))
        self.assertEqual(response.status_code, 401)  # Unauthorized access

    def test_api_orders_list_create(self):
        response = self.client.get(reverse('order-list-create'))
        self.assertEqual(response.status_code, 401)  # Unauthorized access

    def test_api_statements_list(self):
        response = self.client.get(reverse('statement-list'))
        self.assertEqual(response.status_code, 401)  # Unauthorized access
