# module_human_resources/views.py
from ceta.module_generic.views import *
from .serializers import *
from .models import *

class CategoryViewSet(ModelGenericView):
    serializer_class = CategorySerializer
    model = Category
    def get_queryset(self):        
        return Category.objects.filter(is_active = True)

class EmployeeViewSet(ModelGenericView):
    model = Employee
    serializer_class = EmployeeSerializer
    def get_queryset(self):        
        return Employee.objects.filter(is_active = True)