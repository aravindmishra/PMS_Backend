from rest_framework import serializers
from .models import CustomerDetails, PurchaseDetails, BillDetails

class AddCustomerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name','mobile_no')
        model = CustomerDetails

class AddPurchaseDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('customer_id','medicine_id','purchased_qty')
        model = PurchaseDetails

class AddBillDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('customer_id','bill_data')
        model = BillDetails

class PurchaseDetailsListSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField()
    mobile_no = serializers.CharField()
    medicine_name = serializers.CharField()
    class Meta:
        fields = ('customer_name','mobile_no','medicine_name','purchased_qty','created_date')
        model = PurchaseDetails

class BillDetailsListSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    mobile_no = serializers.CharField()
    class Meta:
        fields = ('bill_no','name','mobile_no','bill_data','created_date')
        model = BillDetails

class BillValidSerializer(serializers.Serializer):
    name = serializers.CharField()
    mobile_no = serializers.IntegerField()
    bill_medicine_list = serializers.JSONField()

class GetIdSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()