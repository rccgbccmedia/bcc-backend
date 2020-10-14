from rest_framework import serializers
from .models import User
from phonenumber_field.serializerfields import PhoneNumberField
from dj_rest_auth.serializers import LoginSerializer



class UserRegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    phone = PhoneNumberField(required=True)
    class Meta:
        model=User
        fields=['id','email','address','password','first_name','last_name','phone']
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'address', 'phone']
        read_only_fields = ['email']

class UserLoginSerializer(LoginSerializer):
    username = None
    class Meta: 
        model = User
        fields = ['email', 'password']