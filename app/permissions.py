from rest_framework import permissions


class IsCaseParticipant(permissions.BasePermission):
    '''
    Custom permission to only allow clients and assigned staff to access their cases.
    '''
    def has_object_permission(self, request, view, obj):
        # Проверяем, является ли пользователь клиентом этого дела
        if hasattr(obj, 'client') and hasattr(request.user, 'client_profile'):
            if obj.client == request.user.client_profile:
                return True
        
        # Проверяем, является ли пользователь назначенным сотрудником
        if hasattr(obj, 'assigned_to') and hasattr(request.user, 'staff_profile'):
            if obj.assigned_to == request.user.staff_profile:
                return True
        
        # Если пользователь - staff, разрешаем доступ ко всем делам
        if hasattr(request.user, 'staff_profile'):
            return True
        
        return False


class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    Разрешает редактировать объект только владельцу.
    '''
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Проверяем владельца через связь с User
        if hasattr(obj, 'user'):
            return obj.user == request.user
        
        return False


class IsStaffUser(permissions.BasePermission):
    '''
    Разрешает доступ только сотрудникам.
    '''
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and hasattr(request.user, 'staff_profile')