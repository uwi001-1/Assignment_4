from rest_framework.permissions import BasePermission
from task.models import Task

class taskPermission(BasePermission):
    def has_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        
        if request.method in ['GET', 'PUT', 'PATCH']:
            return obj.assigned_to == request.user   #Only if it's their task
        
        return False