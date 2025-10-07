from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ['name']

    def __str__(self):
        return self.name


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='client_profile')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    messenger = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return self.name


class Request(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_review', 'На рассмотрении'),
        ('contacted', 'Связались'),
        ('converted', 'Преобразована в дело'),
        ('rejected', 'Отклонена'),
    ]
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"{self.subject} - {self.get_status_display()}"


# model would represent the legal cases that are being handled by the firm
class Case(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новое'),
        ('in_progress', 'В работе'),
        ('on_hold', 'Приостановлено'),
        ('completed', 'Завершено'),
        ('closed', 'Закрыто'),
    ]
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="cases")
    title = models.CharField(max_length=200)
    case_number = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='new')
    description = models.TextField()
    assigned_to = models.ForeignKey("Staff", on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_cases')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Дело"
        verbose_name_plural = "Дела"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['case_number']),
            models.Index(fields=['status']),
            models.Index(fields=['created_at']),
            models.Index(fields=['client', 'status']),
        ]

    def __str__(self):
        return f"{self.title} - {self.case_number}"


# manage the people working at the law firm
class Staff(models.Model):
    ROLE_CHOICES = [
        ('lawyer', 'Юрист'),
        ('paralegal', 'Помощник юриста'),
        ('manager', 'Менеджер'),
        ('admin', 'Администратор'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='staff_profile')
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='lawyer')
    phone = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = ['name']
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['role']),
        ]

    def __str__(self):
        return f"{self.name} ({self.get_role_display()})"


# manage the appointments
class Appointment(models.Model):
    case = models.ForeignKey(
        Case, on_delete=models.CASCADE, related_name="appointments"
    )
    subject = models.CharField(max_length=200)
    meeting_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    notes = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Встреча"
        verbose_name_plural = "Встречи"
        ordering = ['-meeting_date']
        indexes = [
            models.Index(fields=['meeting_date']),
            models.Index(fields=['case', 'meeting_date']),
        ]

    def __str__(self):
        return f"{self.subject} - {self.meeting_date.strftime('%d.%m.%Y')}"


class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = "О компании"
        verbose_name_plural = "О компании"

    def __str__(self):
        return self.title
