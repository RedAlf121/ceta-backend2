# module_generic/views.py
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.mixins import DestroyModelMixin
from rest_framework.viewsets import ModelViewSet
from django.db.models import Model
class GeneralView(
        ModelViewSet
    ):
    model:Model = None
    serializer_class = None
    lookup_field = 'pk'
    def get_queryset(self):
        value = self.queryset
        if self.queryset is None:
            value = self.model.objects.all()
            return value


class AllowedGeneralView(GeneralView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

class LogicDelete(DestroyModelMixin):
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

class ModelGenericView(AllowedGeneralView,LogicDelete):
    def get_queryset(self):
        value = self.queryset
        if self.queryset is None:
            value = self.model.objects.filter(is_active=True)
        return value
