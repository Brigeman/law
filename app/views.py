from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
# Rate limiting требует Redis в production
# from django_ratelimit.decorators import ratelimit
# from django.utils.decorators import method_decorator
from .models import Service,Client, Request, Case, Staff, Appointment, About
from .serializers import (
    ServiceSerializer, ClientSerializer, RequestSerializer, 
    CaseSerializer, StaffSerializer, AppointmentSerializer, 
    AboutSerializer, RegisterSerializer, LoginSerializer, UserSerializer
)
from .permissions import IsCaseParticipant, IsOwnerOrReadOnly, IsStaffUser


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['is_active']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price', 'created_at']
    
    def get_queryset(self):
        # Показываем только активные услуги неаутентифицированным пользователям
        if self.request.user.is_authenticated:
            return Service.objects.all()
        return Service.objects.filter(is_active=True)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.select_related('user').prefetch_related('cases')
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsStaffUser]
    search_fields = ['name', 'email', 'company_name', 'phone']
    ordering_fields = ['name', 'created_at']


# TODO: Включить rate limiting после настройки Redis
# @method_decorator(ratelimit(key='ip', rate='20/h', method='POST'), name='create')
class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.select_related('client')
    serializer_class = RequestSerializer
    permission_classes = [AllowAny]  # Разрешаем всем отправлять заявки
    filterset_fields = ['status', 'client']
    search_fields = ['subject', 'description']
    ordering_fields = ['created_at', 'updated_at']
    
    def get_queryset(self):
        # Оптимизация с select_related
        queryset = Request.objects.select_related('client')
        
        # Сотрудники видят все заявки, клиенты только свои
        if hasattr(self.request.user, 'staff_profile'):
            return queryset
        elif hasattr(self.request.user, 'client_profile'):
            return queryset.filter(client=self.request.user.client_profile)
        return Request.objects.none()


class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.select_related('client', 'assigned_to').prefetch_related('appointments')
    serializer_class = CaseSerializer
    permission_classes = [IsAuthenticated, IsCaseParticipant]
    filterset_fields = ['status', 'assigned_to', 'client']
    search_fields = ['title', 'case_number', 'description']
    ordering_fields = ['created_at', 'updated_at', 'case_number']

    def get_queryset(self):
        # Оптимизация с select_related
        queryset = Case.objects.select_related('client', 'assigned_to').prefetch_related('appointments')
        
        # Сотрудники видят все дела, клиенты только свои
        if hasattr(self.request.user, 'staff_profile'):
            return queryset
        elif hasattr(self.request.user, 'client_profile'):
            return queryset.filter(client=self.request.user.client_profile)
        return Case.objects.none()


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.select_related('user')
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['role', 'is_active']
    search_fields = ['name', 'email']
    ordering_fields = ['name', 'created_at']
    
    def get_queryset(self):
        # Оптимизация и показываем только активных сотрудников
        queryset = Staff.objects.select_related('user')
        return queryset.filter(is_active=True)


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.select_related('case', 'case__client', 'case__assigned_to')
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['is_completed', 'case']
    search_fields = ['subject', 'notes']
    ordering_fields = ['meeting_date', 'created_at']

    def get_queryset(self):
        # Оптимизация с select_related
        queryset = Appointment.objects.select_related('case', 'case__client', 'case__assigned_to')
        
        # Сотрудники видят все встречи, клиенты только по своим делам
        if hasattr(self.request.user, 'staff_profile'):
            return queryset
        elif hasattr(self.request.user, 'client_profile'):
            return queryset.filter(case__client=self.request.user.client_profile)
        return Appointment.objects.none()

    def perform_create(self, serializer):
        try:
            instance = serializer.save()
            # send email notification
            client_email = instance.case.client.email
            send_mail(
                'Назначение встречи',
                f'У вас назначена встреча на {instance.meeting_date}.',
                settings.DEFAULT_FROM_EMAIL,
                [client_email],
                fail_silently=True,  # Не падаем при ошибке отправки email
            )
        except Exception as e:
            # Логируем ошибку, но не падаем
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f'Ошибка при отправке email: {str(e)}')


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


# Authentication Views
# TODO: Включить rate limiting после настройки Redis
# @method_decorator(ratelimit(key='ip', rate='5/h', method='POST'), name='post')
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            
            return Response({
                'user': UserSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': 'Пользователь успешно зарегистрирован'
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TODO: Включить rate limiting после настройки Redis
# @method_decorator(ratelimit(key='ip', rate='10/h', method='POST'), name='post')
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'user': UserSerializer(user).data,
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'message': 'Вход выполнен успешно'
                }, status=status.HTTP_200_OK)
            
            return Response({
                'error': 'Неверные учётные данные'
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response({
                    'message': 'Выход выполнен успешно'
                }, status=status.HTTP_200_OK)
            
            return Response({
                'error': 'Refresh token не предоставлен'
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)