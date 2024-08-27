# module_accounting/views.py
from ceta.module_generic.views import AllowedGeneralView 
from .serializers import *
from .models import *

class BillViewSet(AllowedGeneralView):
    serializer_class = BillSerializer
    model=Bill

class ReceiptViewSet(AllowedGeneralView):
    model = Receipt
    serializer_class = ReceiptSerializer

class RemunerationViewSet(AllowedGeneralView):
    model = Remuneration
    serializer_class = RemunerationSerializer
