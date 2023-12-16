from rest_framework import serializers
from .models import User,Profile,Storesong

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =User
#         # field = [
#         #     "id",
#         # ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ='__all__'

class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields ='__all__'

class storesongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storesong
        fields ='__all__'