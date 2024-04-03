from django.contrib import admin
from .models import Client, Request, Case, Staff, Appointment


admin.site.register(Client)
admin.site.register(Request)
admin.site.register(Case)
admin.site.register(Staff)
admin.site.register(Appointment)
