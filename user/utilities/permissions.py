from rest_framework.permissions import BasePermission

ADMIN = 1
USER = 2

def IsAunthenticated(request):
    return bool(request.user and request.user.is_authenticated)

def AdminLevel(request):
    return bool(IsAunthenticated(request) and request.user.role in [ADMIN])

