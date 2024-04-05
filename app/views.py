from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Client, Request, Case, Staff, Appointment
from .serializers import ClientSerializer, RequestSerializer, CaseSerializer, StaffSerializer, AppointmentSerializer
from django.core.mail import send_mail
from django.conf import settings


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        # send email notification
        client_email = instance.case.client.email
        send_mail(
            'Назначение встречи',
            f'У вас назначена встреча на {instance.meeting_date}.',
            settings.DEFAULT_FROM_EMAIL,  # EMAIL_HOST_USER
            [client_email],
            fail_silently=False,
        )
