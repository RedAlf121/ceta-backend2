# module_accounting/serializers.py
from rest_framework import fields 
from rest_framework_json_api import serializers
from collections import OrderedDict
from ceta.validations import *
from .models import *
from ceta.module_contract.serializers import PaymentTermSerializer  

class BillSerializer(serializers.ModelSerializer):  
    fk_id_payterm = PaymentTermSerializer()
  
    class Meta:
        model = Bill
        fields = '__all__'
        read_only_fields = ('id_bill',)
        depth=1

class ReceiptSerializer(serializers.ModelSerializer):  
    fk_id_bill = BillSerializer()
  
    class Meta:
        model = Receipt
        fields = '__all__'
        read_only_fields = ('id_rec',)
        depth=1

class RemunerationSerializer(serializers.ModelSerializer):  
    fk_id_bill = BillSerializer()
  
    class Meta:
        model = Remuneration
        fields = '__all__'
        read_only_fields = ('id_rem',)
        depth=1