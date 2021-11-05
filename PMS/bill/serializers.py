from rest_framework import serializers
from .models import CustomerDetails, PurchaseDetails

class AddCustomerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name','mobile_no')
        model = CustomerDetails

class AddPurchaseDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('customer_id','medicine_id','purchased_qty')
        model = PurchaseDetails

class PurchaseDetailsListSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField()
    mobile_no = serializers.CharField()
    medicine_name = serializers.CharField()
    class Meta:
        fields = ('customer_name','mobile_no','medicine_name','purchased_qty','created_date')
        model = PurchaseDetails


class BillValidSerializer(serializers.Serializer):
    name = serializers.CharField()
    mobile_no = serializers.IntegerField()
    bill_medicine_list = serializers.JSONField()

class GetIdSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()