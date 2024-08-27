# module_user/views.py

import json
from ceta.module_generic.views import ModelGenericView,AllowedGeneralView
from rest_framework.mixins import DestroyModelMixin
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.status import *
from django.contrib.auth.models import User,Group
from .serializers import UserSerializer,RoleSerializer

class UserViewSet(ModelGenericView):
    model = User
    serializer_class = UserSerializer

class RoleViewSet(AllowedGeneralView):
    model = Group
    serializer_class = RoleSerializer

