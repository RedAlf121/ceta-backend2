# module_offer/views.py

from ceta.module_generic.views import ModelGenericView
from .serializers import *
from .models import *
class TrainingViewSet(ModelGenericView):
    model = Training
    serializer_class = TrainingSerializer

class ServiceViewSet(ModelGenericView):
    model = Service
    serializer_class = ServiceSerializer