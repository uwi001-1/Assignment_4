from rest_framework import viewsets
from ..models import CustomUser
from ..serializers.user_serializers import UserListSerializers, UserRetrieveSerializers, UserWriteSerializers

from user.utilities.pagination import MyPageNumberPagination

class userViewsets(viewsets.ModelViewSet):
    serializer_class = UserListSerializers
    queryset = CustomUser.objects.all().order_by('-id')
    pagination_class = MyPageNumberPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return UserWriteSerializers
        elif self.action == 'retrieve':
            return UserRetrieveSerializers
        return super().get_serializer_class()