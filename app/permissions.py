from rest_framework import permissions


class IsCaseParticipant(permissions.BasePermission):
    '''
    Custom permission to only allow clients to access their cases.
    '''
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'client') and obj.client == request.user:
            return True
        elif hasattr(obj, 'staff') and obj.assigned_to == request.user:
            return True
        return False