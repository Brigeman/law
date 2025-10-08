from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from django.core import mail
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Service, Client, Appointment, Case, Staff, About, Request


# ========== Authentication Tests ==========
class AuthenticationTests(APITestCase):
    """Тесты аутентификации и авторизации"""
    
    def test_user_registration(self):
        """Тест регистрации нового пользователя"""
        url = reverse('auth-register')
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'SecurePass123!',
            'password2': 'SecurePass123!',
            'first_name': 'New',
            'last_name': 'User'
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertIn('user', response.data)
        self.assertEqual(response.data['user']['username'], 'newuser')
        self.assertEqual(User.objects.count(), 1)
    
    def test_registration_password_mismatch(self):
        """Тест регистрации с несовпадающими паролями"""
        url = reverse('auth-register')
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'SecurePass123!',
            'password2': 'DifferentPass123!',
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Проверяем наличие ошибки (может быть в details или напрямую)
        self.assertTrue('password' in str(response.data))
    
    def test_registration_duplicate_email(self):
        """Тест регистрации с существующим email"""
        User.objects.create_user(username='existing', email='test@example.com', password='pass')
        
        url = reverse('auth-register')
        data = {
            'username': 'newuser',
            'email': 'test@example.com',
            'password': 'SecurePass123!',
            'password2': 'SecurePass123!',
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Проверяем наличие ошибки email
        self.assertTrue('email' in str(response.data))
    
    def test_user_login(self):
        """Тест входа пользователя"""
        user = User.objects.create_user(username='testuser', password='TestPass123!')
        
        url = reverse('auth-login')
        data = {
            'username': 'testuser',
            'password': 'TestPass123!'
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertEqual(response.data['user']['username'], 'testuser')
    
    def test_login_invalid_credentials(self):
        """Тест входа с неверными данными"""
        User.objects.create_user(username='testuser', password='TestPass123!')
        
        url = reverse('auth-login')
        data = {
            'username': 'testuser',
            'password': 'WrongPassword'
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('error', response.data)
    
    def test_get_current_user(self):
        """Тест получения текущего пользователя"""
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass')
        self.client.force_authenticate(user=user)
        
        url = reverse('auth-current-user')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')
        self.assertEqual(response.data['email'], 'test@example.com')
    
    def test_logout(self):
        """Тест выхода пользователя"""
        user = User.objects.create_user(username='testuser', password='pass')
        refresh = RefreshToken.for_user(user)
        
        self.client.force_authenticate(user=user)
        url = reverse('auth-logout')
        data = {'refresh': str(refresh)}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('message', response.data)


# ========== Model Tests ==========
class ServiceAPITests(APITestCase):
    def setUp(self):
        # Create test data
        self.service = Service.objects.create(name='Test Service', description='Test description')

    def test_get_services(self):
        # Test to get all services
        url = reverse('service-list')  # Use reverse() to get the URL for the service list view
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ClientAPITests(APITestCase):
    def setUp(self):
        # Create staff user
        self.user = User.objects.create_user(username='staffuser', password='testpassword')
        self.staff = Staff.objects.create(
            user=self.user,
            name='Staff Member',
            email='staff@example.com',
            role='admin'
        )
        self.client.force_authenticate(user=self.user)

    def test_get_clients(self):
        """Тест получения списка клиентов (только для staff)"""
        url = reverse('client-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_client(self):
        """Тест создания клиента"""
        url = reverse('client-list')
        data = {
            'name': 'Test Client',
            'email': 'client@example.com',
            'company_name': 'Test Company',
            'phone': '1234567890',
            'messenger': 'Test Messenger'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(Client.objects.get().name, 'Test Client')


class AppointmentTests(APITestCase):
    def setUp(self):
        # Create staff user
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.staff = Staff.objects.create(
            user=self.user,
            name='Staff Member',
            email='staff@example.com',
            role='lawyer'
        )

        # Create client
        self.client_obj = Client.objects.create(
            name="Test Client",
            email="client@example.com",
            company_name="Test Company",
            phone="1234567890",
            messenger="Test Messenger"
        )

        # Create case
        self.case = Case.objects.create(
            client=self.client_obj,
            title="Test Case",
            case_number="TC-123",
            status="new",
            description="Test Case Description for testing purposes"
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_appointment_email_sent(self):
        # Prepare test data with future date
        from django.utils import timezone
        from datetime import timedelta
        future_date = (timezone.now() + timedelta(days=7)).isoformat()
        
        data = {
            'case': self.case.id,
            'subject': 'Test Appointment',
            'meeting_date': future_date,
            'notes': 'Test Notes'
        }

        # Create appointment
        response = self.client.post('/appointments/', data, format='json')

        # Проверки
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        self.assertEqual(Appointment.objects.count(), 1)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Назначение встречи')


class CaseTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.staff = Staff.objects.create(
            user=self.user,
            name='Staff Member',
            email='staff@example.com',
            role='lawyer'
        )
        self.client.force_authenticate(user=self.user)
        self.client_obj = Client.objects.create(name="Client", email="client@example.com")

    def test_create_case(self):
        """Тест создания дела"""
        data = {
            'title': 'New Case',
            'case_number': 'NC-12345',
            'status': 'new',
            'client': self.client_obj.id,
            'description': 'Test Case Description for testing purposes'
        }

        response = self.client.post('/cases/', data, format='json')

        if response.status_code != status.HTTP_201_CREATED:
            print(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Case.objects.count(), 1)


class StaffTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='stafftestuser', email='stafftest@example.com', password='password')
        self.client.force_authenticate(user=self.user)

    def test_get_staff(self):
        """Тест получения списка сотрудников"""
        url = reverse('staff-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AboutTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='abouttestuser', email='abouttest@example.com', password='password')
        self.client.force_authenticate(user=self.user)

    def test_get_about(self):
        url = reverse('about-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# ========== Validation Tests ==========
class ValidationTests(APITestCase):
    """Тесты валидации данных"""
    
    def setUp(self):
        # Create authenticated user for tests
        self.user = User.objects.create_user(username='validationtestuser', password='pass')
        self.client.force_authenticate(user=self.user)
    
    def test_service_validation_short_name(self):
        """Тест валидации короткого имени услуги"""
        url = reverse('service-list')
        data = {'name': 'AB', 'description': 'Valid description text here'}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('name' in str(response.data))
    
    def test_service_validation_short_description(self):
        """Тест валидации короткого описания"""
        url = reverse('service-list')
        data = {'name': 'Valid Name', 'description': 'Short'}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('description' in str(response.data))
    
    def test_service_validation_negative_price(self):
        """Тест валидации отрицательной цены"""
        url = reverse('service-list')
        data = {'name': 'Valid Name', 'description': 'Valid description text', 'price': -100}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('price' in str(response.data))
    
    def test_client_validation_invalid_email(self):
        """Тест валидации неверного email"""
        user = User.objects.create_user(username='staff', password='pass')
        staff = Staff.objects.create(user=user, name='Staff', email='staff@example.com', role='admin')
        self.client.force_authenticate(user=user)
        
        url = reverse('client-list')
        data = {'name': 'Test Client', 'email': 'invalid-email'}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('email' in str(response.data))
    
    def test_request_validation_short_subject(self):
        """Тест валидации короткой темы заявки"""
        url = reverse('request-list')
        data = {'subject': 'Hi', 'description': 'Valid long description text here for testing'}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('subject' in str(response.data))
    
    def test_case_validation_invalid_case_number(self):
        """Тест валидации номера дела"""
        user = User.objects.create_user(username='staff', password='pass')
        staff = Staff.objects.create(user=user, name='Staff', email='staff@example.com', role='admin')
        client = Client.objects.create(name='Client', email='client@example.com')
        self.client.force_authenticate(user=user)
        
        url = reverse('case-list')
        data = {
            'title': 'Test Case',
            'case_number': 'invalid@number',  # содержит недопустимый символ
            'description': 'Valid long description for the case',
            'client': client.id,
            'status': 'new'
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('case_number' in str(response.data))


# ========== Permission Tests ==========
class PermissionTests(APITestCase):
    """Тесты прав доступа"""
    
    def setUp(self):
        # Создаем пользователя-клиента
        self.client_user = User.objects.create_user(username='client_user', password='pass')
        self.client_profile = Client.objects.create(
            user=self.client_user,
            name='Client Name',
            email='client@example.com'
        )
        
        # Создаем пользователя-сотрудника
        self.staff_user = User.objects.create_user(username='staff_user', password='pass')
        self.staff_profile = Staff.objects.create(
            user=self.staff_user,
            name='Staff Name',
            email='staff@example.com',
            role='lawyer'
        )
        
        # Создаем дело
        self.case = Case.objects.create(
            client=self.client_profile,
            title='Test Case',
            case_number='TC-001',
            description='Test case description text',
            status='new'
        )
    
    def test_client_can_access_own_case(self):
        """Клиент может видеть свои дела"""
        self.client.force_authenticate(user=self.client_user)
        url = reverse('case-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
    
    def test_staff_can_access_all_cases(self):
        """Сотрудник может видеть все дела"""
        self.client.force_authenticate(user=self.staff_user)
        url = reverse('case-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
    
    def test_unauthenticated_cannot_access_cases(self):
        """Неаутентифицированный пользователь не может видеть дела"""
        url = reverse('case-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_only_staff_can_access_clients(self):
        """Только сотрудники могут получить список клиентов"""
        # Пробуем без аутентификации
        url = reverse('client-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        # Пробуем как клиент
        self.client.force_authenticate(user=self.client_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        # Пробуем как сотрудник
        self.client.force_authenticate(user=self.staff_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# ========== Security Tests ==========
class SecurityTests(APITestCase):
    """Тесты безопасности"""
    
    def setUp(self):
        # Create authenticated user for tests
        self.user = User.objects.create_user(username='securitytestuser', password='pass')
        self.client.force_authenticate(user=self.user)
    
    def test_xss_protection_in_description(self):
        """Тест защиты от XSS в описании"""
        url = reverse('service-list')
        data = {
            'name': 'Test Service',
            'description': '<script>alert("XSS")</script>Valid description text here'
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Проверяем, что script тег был удален
        service = Service.objects.get(id=response.data['id'])
        self.assertNotIn('<script>', service.description)
        self.assertNotIn('</script>', service.description)
    
    def test_sql_injection_protection(self):
        """Тест защиты от SQL injection"""
        url = reverse('service-list')
        data = {
            'name': "'; DROP TABLE services; --",
            'description': 'Valid description text for testing'
        }
        response = self.client.post(url, data, format='json')
        
        # Django ORM защищает от SQL injection
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Проверяем, что таблица не удалена
        self.assertEqual(Service.objects.count(), 1)
    
    def test_password_hashing(self):
        """Пароли должны быть захешированы"""
        user = User.objects.create_user(username='testuser', password='plainpassword')
        self.assertNotEqual(user.password, 'plainpassword')
        self.assertTrue(user.password.startswith('pbkdf2_sha256'))
