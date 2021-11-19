from rest_framework import serializers
from .models import UserDetails

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name','dob','mobile_no','email_id','password','status')
        model = UserDetails

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name','dob','mobile_no','email_id','status')
        model = UserDetails

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('user_id','name','dob','mobile_no','email_id','status','created_date')
        model = UserDetails