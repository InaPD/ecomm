from rest_framework import serializers
from myapp.models import Product,UserAddress,EcommUser

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'



class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserAddress
        fields='__all__'



class EcommUserSerializer(serializers.ModelSerializer):
    address = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=False,
        queryset=UserAddress.objects.all())

    class Meta:
        model=EcommUser
        fields=('name','last_name','email','credit_card','created','slug','address')





