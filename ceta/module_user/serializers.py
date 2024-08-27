from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User,Group

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        depth=1


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
