from rest_framework.permissions import BasePermission

ADMIN = 1
REGULAR_USER = 2

def IsAunthenticated(request):
    return bool(request.user and request.user.is_authenticated)

def AdminLevel(request):
    return bool(IsAunthenticated(request) and request.user.role in [ADMIN])

def isOwner(request):
    if str(request.user.id) == str(request.data.get('user')):
        return True
    elif len(request.data) == 0 and len(request.POST) == 0:
        return True
    return False

class bookPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list']:
            return True
        elif view.action in ['retrieve']:
            return isOwner(request)
        elif view.action in ['create', 'update']:
            return isOwner(request)   #second level
            # return ObjectBOwner(request)   third level
        elif view.action == ['partial_update']:
            return view.get_object().user_id == request.user.id
        elif view.action == ['destroy']:
            return isOwner(request)
