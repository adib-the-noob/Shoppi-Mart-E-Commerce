from rest_framework import serializers
from .models import Address, MyUser as User
from django.db.models import Q



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
    name = serializers.SerializerMethodField()

    def get_name(self, user: User):
        return user.name

    class Meta:
        model = User
        fields = ['name', 'phone','email']

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ('email','password')

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = User.objects.filter(email=email).first()
        if user is None:
            raise serializers.ValidationError({'email': 'User does not exist.'})
        if not user.check_password(password):
            raise serializers.ValidationError({'password': 'Incorrect password.'})
        return attrs