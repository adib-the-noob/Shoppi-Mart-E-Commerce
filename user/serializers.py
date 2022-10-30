from rest_framework import serializers
from .models import Address, MyUser



class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['address', 'place', 'zipcode', 'phone']

        
class UserProfileSerializer(serializers.ModelSerializer):
    address = UserAddressSerializer(many=True, read_only=True)
    class Meta:
        model = MyUser
        fields = ['email', 'name', 'phone', 'address']
