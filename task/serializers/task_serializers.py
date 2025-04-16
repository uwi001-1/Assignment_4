from rest_framework import serializers
from ..models import Task
from user.models import CustomUser


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'role']
        ref_name = 'user_task'

class TaskListSerializers(serializers.ModelSerializer):
    genre = UserSerializers(read_only = True)
    class Meta:
        model = Task
        fields = '__all__'

class TaskRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

def create(self, validated_data):  #Overwrite CREATE
    return super().create(validated_data)

def update(self, instance, validated_data):
    return super().update(instance, validated_data)