# module_contract/views.py

from ceta.module_generic.views import ModelGenericView
from .serializers import *
from .models import *
class ClientViewSet(ModelGenericView):
    model = Client
    serializer_class = ClientSerializer

class ContractViewSet(ModelGenericView):
    model = Contract
    serializer_class = ContractSerializer

class PaymentTermViewSet(ModelGenericView):
    model = PaymentTerm

class PaymentEmployeeViewSet(ModelGenericView):
    #permission_classes = (IsAuthenticated,)
    model = PaymentEmployee
    serializer_class = PaymentEmployeeSerializer
