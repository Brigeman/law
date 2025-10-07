"""
Custom exception handlers for the API
"""
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    """
    Кастомная обработка ошибок API.
    Логирует все ошибки и возвращает понятные сообщения.
    """
    # Вызываем стандартный обработчик
    response = exception_handler(exc, context)

    # Если response уже создан, возвращаем его
    if response is not None:
        # Логируем ошибку
        logger.error(
            f"API Error: {exc.__class__.__name__} - {str(exc)}",
            extra={
                'view': context.get('view'),
                'request': context.get('request'),
            }
        )
        
        # Добавляем дополнительную информацию в response
        response.data = {
            'error': True,
            'message': str(exc),
            'details': response.data if isinstance(response.data, dict) else {'detail': response.data},
            'status_code': response.status_code
        }
        
        return response
    
    # Обрабатываем необработанные исключения
    logger.critical(
        f"Unhandled exception: {exc.__class__.__name__} - {str(exc)}",
        exc_info=True,
        extra={
            'view': context.get('view'),
            'request': context.get('request'),
        }
    )
    
    return Response(
        {
            'error': True,
            'message': 'Внутренняя ошибка сервера',
            'details': {'detail': str(exc)},
            'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )

