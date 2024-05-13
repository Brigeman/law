from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    messenger = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Request(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


# model would represent the legal cases that are being handled by the firm
class Case(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="cases")
    title = models.CharField(max_length=200)
    case_number = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey("Staff", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.case_number}"


# manage the people working at the law firm
class Staff(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


# manage the appointments
class Appointment(models.Model):
    case = models.ForeignKey(
        Case, on_delete=models.CASCADE, related_name="appointments"
    )
    subject = models.CharField(max_length=200)
    meeting_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.subject


class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


# TODO  Implementing User Authentication