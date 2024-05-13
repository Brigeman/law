from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, ClientViewSet, RequestViewSet, CaseViewSet, StaffViewSet, AppointmentViewSet, AboutViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'requests', RequestViewSet)
router.register(r'cases', CaseViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'about', AboutViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
