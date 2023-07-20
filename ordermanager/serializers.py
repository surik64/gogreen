from django.shortcuts import render 
from rest_framework import viewsets, serializers
from .models import OrderModel
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser

# Create your views here.  
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields  = '__all__'
   
