"""
Utility functions for the app
"""
import bleach
import re


def sanitize_html(text):
    """
    Очистка HTML от потенциально опасных тегов и атрибутов.
    Защита от XSS атак.
    """
    if not text:
        return text
    
    # Разрешенные теги
    allowed_tags = ['p', 'br', 'strong', 'em', 'u', 'a', 'ul', 'ol', 'li']
    
    # Разрешенные атрибуты
    allowed_attributes = {
        'a': ['href', 'title'],
    }
    
    # Очищаем HTML
    cleaned = bleach.clean(
        text,
        tags=allowed_tags,
        attributes=allowed_attributes,
        strip=True
    )
    
    return cleaned


def validate_phone_number(phone):
    """
    Валидация номера телефона.
    Возвращает только цифры.
    """
    if not phone:
        return None
    
    # Убираем все нецифровые символы
    phone_digits = re.sub(r'\D', '', phone)
    
    if len(phone_digits) < 10 or len(phone_digits) > 15:
        raise ValueError("Номер телефона должен содержать от 10 до 15 цифр")
    
    return phone_digits


def validate_email_format(email):
    """
    Валидация формата email.
    """
    if not email:
        return False
    
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_regex, email))

