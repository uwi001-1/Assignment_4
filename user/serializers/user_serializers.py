from rest_framework import serializers
from ..models import CustomUser

class UserListSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class UserRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class UserWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'