from django.shortcuts import render
from rest_framework_simplejwt import views as jwt_views,  serializers as jwt_serializers
# from rest_framework_simplejwt import serializers as jwt_serializers
from rest_framework import serializers
 
from django.contrib.auth import get_user_model


User =get_user_model()

# Create your views here.


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer to view all Users
    """
 
    class Meta:
        model = User
        fields = "__all__" 
       

class  SignInSerializer(jwt_serializers.TokenObtainPairSerializer):
    ...
     
    #  def validate(self, attrs):
    #     data = super().validate(attrs)
    #     # user = UserSerializer(self.user ).data
    #     # data.update(user)
          
        
    #     return data



class SigninView(jwt_views.TokenObtainPairView):
    serializer_class = SignInSerializer


    
