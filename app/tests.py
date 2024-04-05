from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Client
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class ClientAPITests(APITestCase):
    def setUp(self):
        # Создание пользователя и токена для тестирования аутентификации
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_clients(self):
        # Тест на получение списка клиентов
        url = reverse('client-list')  # Используйте reverse для получения URL из имени view
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_client(self):
        # Тест на создание нового клиента
        url = reverse('client-list')
        data = {'name': 'Test Client', 'email': 'client@example.com', 'company_name': 'Test Company', 'phone': '1234567890', 'messenger': 'Test Messenger'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(Client.objects.get().name, 'Test Client')
