from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import Service, Client, Request, Case, Staff, Appointment, About
from .utils import sanitize_html


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"
    
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Название услуги должно быть не менее 3 символов")
        if len(value) > 100:
            raise serializers.ValidationError("Название услуги не должно превышать 100 символов")
        return value.strip()
    
    def validate_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Описание должно быть не менее 10 символов")
        if len(value) > 5000:
            raise serializers.ValidationError("Описание не должно превышать 5000 символов")
        # Защита от XSS
        return sanitize_html(value.strip())
    
    def validate_price(self, value):
        if value is not None and value < 0:
            raise serializers.ValidationError("Цена не может быть отрицательной")
        if value is not None and value > 9999999.99:
            raise serializers.ValidationError("Цена слишком большая")
        return value


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
        read_only_fields = ('user', 'created_at', 'updated_at')
    
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Имя должно быть не менее 2 символов")
        if len(value) > 100:
            raise serializers.ValidationError("Имя не должно превышать 100 символов")
        return value.strip()
    
    def validate_email(self, value):
        import re
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, value):
            raise serializers.ValidationError("Неверный формат email")
        return value.lower().strip()
    
    def validate_phone(self, value):
        if value:
            import re
            # Убираем все нецифровые символы
            phone_digits = re.sub(r'\D', '', value)
            if len(phone_digits) < 10 or len(phone_digits) > 15:
                raise serializers.ValidationError("Номер телефона должен содержать от 10 до 15 цифр")
        return value.strip() if value else value


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = "__all__"
        read_only_fields = ('status', 'created_at', 'updated_at')
    
    def validate_subject(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Тема заявки должна быть не менее 5 символов")
        if len(value) > 200:
            raise serializers.ValidationError("Тема заявки не должна превышать 200 символов")
        return value.strip()
    
    def validate_description(self, value):
        if len(value) < 20:
            raise serializers.ValidationError("Описание должно быть не менее 20 символов")
        if len(value) > 10000:
            raise serializers.ValidationError("Описание не должно превышать 10000 символов")
        # Защита от XSS
        return sanitize_html(value.strip())


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = "__all__"
        read_only_fields = ('created_at', 'updated_at')
    
    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Название дела должно быть не менее 5 символов")
        if len(value) > 200:
            raise serializers.ValidationError("Название дела не должно превышать 200 символов")
        return value.strip()
    
    def validate_case_number(self, value):
        import re
        # Формат: буквы и цифры
        if not re.match(r'^[A-Za-z0-9-]+$', value):
            raise serializers.ValidationError("Номер дела может содержать только буквы, цифры и дефис")
        if len(value) < 3 or len(value) > 100:
            raise serializers.ValidationError("Номер дела должен быть от 3 до 100 символов")
        return value.upper().strip()
    
    def validate_description(self, value):
        if len(value) < 20:
            raise serializers.ValidationError("Описание должно быть не менее 20 символов")
        if len(value) > 10000:
            raise serializers.ValidationError("Описание не должно превышать 10000 символов")
        # Защита от XSS
        return sanitize_html(value.strip())


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"
        read_only_fields = ('user', 'created_at', 'updated_at')
    
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Имя должно быть не менее 2 символов")
        if len(value) > 100:
            raise serializers.ValidationError("Имя не должно превышать 100 символов")
        return value.strip()
    
    def validate_email(self, value):
        import re
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, value):
            raise serializers.ValidationError("Неверный формат email")
        return value.lower().strip()
    
    def validate_phone(self, value):
        if value:
            import re
            phone_digits = re.sub(r'\D', '', value)
            if len(phone_digits) < 10 or len(phone_digits) > 15:
                raise serializers.ValidationError("Номер телефона должен содержать от 10 до 15 цифр")
        return value.strip() if value else value


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
        read_only_fields = ('created_at', 'updated_at')
    
    def validate_subject(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Тема встречи должна быть не менее 5 символов")
        if len(value) > 200:
            raise serializers.ValidationError("Тема встречи не должна превышать 200 символов")
        return value.strip()
    
    def validate_meeting_date(self, value):
        from django.utils import timezone
        if value < timezone.now():
            raise serializers.ValidationError("Дата встречи не может быть в прошлом")
        return value
    
    def validate_notes(self, value):
        if value and len(value) > 5000:
            raise serializers.ValidationError("Заметки не должны превышать 5000 символов")
        # Защита от XSS
        return sanitize_html(value.strip()) if value else value


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"
        read_only_fields = ('created_at', 'updated_at')
    
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Заголовок должен быть не менее 3 символов")
        if len(value) > 100:
            raise serializers.ValidationError("Заголовок не должен превышать 100 символов")
        return value.strip()
    
    def validate_description(self, value):
        if len(value) < 20:
            raise serializers.ValidationError("Описание должно быть не менее 20 символов")
        if len(value) > 10000:
            raise serializers.ValidationError("Описание не должно превышать 10000 символов")
        # Защита от XSS
        return sanitize_html(value.strip())


# Auth Serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = ('id',)


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли не совпадают"})
        
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({"email": "Пользователь с таким email уже существует"})
        
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            password=validated_data['password']
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
