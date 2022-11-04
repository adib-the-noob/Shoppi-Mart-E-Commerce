from rest_framework import serializers
from .models import Address, MyUser as User



class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['address', 'place', 'zipcode', 'phone']

class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'name', 'phone', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password1 = attrs.get('password')
        password2 = attrs.pop('password2')
        if password1 != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        return attrs

    def create(self, validated_data):
        user=User.objects.create_user(**validated_data)
        return user
        
        
class UserProfileSerializer(serializers.ModelSerializer):
    address = UserAddressSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['email', 'name', 'phone', 'address']
