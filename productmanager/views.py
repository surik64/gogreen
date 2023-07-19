from django.shortcuts import render
from rest_framework import viewsets, serializers
from .models import ProductModel
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
#from  .filters import CategoryFilter

# Create your views here.  
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields  = '__all__'
   

class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (FormParser,)
