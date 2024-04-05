from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import Client, Appointment, Case
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.core import mail


class ClientAPITests(APITestCase):
    def setUp(self):
        # Create test data
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_clients(self):
        # Test to get all clients
        url = reverse('client-list')  # Use reverse() to get the URL for the client list view
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_client(self):
        # Test to create a new client
        url = reverse('client-list')
        data = {'name': 'Test Client', 'email': 'client@example.com', 'company_name': 'Test Company', 'phone': '1234567890', 'messenger': 'Test Messenger'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(Client.objects.get().name, 'Test Client')


class AppointmentTests(TestCase):
    def setUp(self):
        # Create test data
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.token = Token.objects.create(user=self.user)

        # Create client
        self.client_obj = Client.objects.create(name="Test Client", email="client@example.com",
                                                company_name="Test Company", phone="1234567890",
                                                messenger="Test Messenger")

        # Create case
        self.case = Case.objects.create(client=self.client_obj, title="Test Case", case_number="123", status="Open",
                                        description="Test Case Description")

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_appointment_email_sent(self):
        # Prepare test data
        data = {
            'case': self.case.id,
            'subject': 'Test Appointment',
            'meeting_date': '2023-01-01T12:00:00Z',
            'notes': 'Test Notes'
        }

        # Create appointment
        response = self.client.post('/appointments/', data, format='json')

        # Проверки
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        self.assertEqual(Appointment.objects.count(), 1)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Назначение встречи')