from rest_framework import serializers
from .models import MedicineDetails

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('rack_no','medicine_name','brand','power','price','quantity')
        model = MedicineDetails

class MedicineListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = MedicineDetails