from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="API Documentation",  # Название вашего API
      default_version='v1',  # Версия API
      description="API documentation for my project",  # Описание
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@myproject.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),  # Разрешаем доступ к документации всем пользователям
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),  # Ваши текущие маршруты
    # Маршруты для документации API
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
