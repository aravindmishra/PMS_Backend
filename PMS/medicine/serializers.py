from rest_framework import serializers
from .models import MedicineDetails

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('rack_no','medicine_name','brand','power','price','quantity','status')
        model = MedicineDetails

class MedicineListSerializer(serializers.ModelSerializer):
    purchased_qty = serializers.IntegerField()
    status = serializers.CharField()
    class Meta:
        fields = ('medicine_id','rack_no','medicine_name','brand','power','price','quantity','purchased_qty','status')
        model = MedicineDetails