from rest_framework import serializers
from .models import User
from phonenumber_field.serializerfields import PhoneNumberField



class UserRegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    phone = serializers.PhoneNumberField(required=True)
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
