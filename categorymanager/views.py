from django.shortcuts import render
from rest_framework import viewsets, serializers
from .models import CategoryModel,SubCategoryModel
from  .filters import CategoryFilter
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser

# Create your views here.
class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields  = '__all__'
       
class SubCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoryModel
        fields = '__all__'
        # depth = 1

class CategoryViewSet(viewsets.ModelViewSet):
    filterset_class =  CategoryFilter
    queryset = CategoryModel.objects.all()
    serializer_class = CatSerializer
    # http_method_names =['get']
   

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategoryModel.objects.all()
    serializer_class = SubCatSerializer
    parser_classes = ( MultiPartParser, FormParser)

    
    