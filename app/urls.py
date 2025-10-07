from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    ServiceViewSet, ClientViewSet, RequestViewSet, CaseViewSet, 
    StaffViewSet, AppointmentViewSet, AboutViewSet,
    RegisterView, LoginView, LogoutView, CurrentUserView
)

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
    
    # Authentication endpoints
    path('auth/register/', RegisterView.as_view(), name='auth-register'),
    path('auth/login/', LoginView.as_view(), name='auth-login'),
    path('auth/logout/', LogoutView.as_view(), name='auth-logout'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='auth-refresh'),
    path('auth/user/', CurrentUserView.as_view(), name='auth-current-user'),
]
