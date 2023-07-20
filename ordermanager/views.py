from django.shortcuts import render 
from rest_framework import viewsets, serializers
from .models import OrderModel, CartModel, WishlistModel
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
#from  .filters import CategoryFilter



# Create your views here.  
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields  = '__all__'

# Create your views here.  
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields  = '__all__'

  
class WishlsitSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistModel
        fields  = '__all__'

  



class OrderViewSet(viewsets.ModelViewSet):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer           #MultiPartParser is used for videos,images for posting.
    parser_classes = (FormParser,MultiPartParser)  #FormParser is used for images format while posting images
    



class CartViewSet(viewsets.ModelViewSet):
    queryset = CartModel.objects.all()
    serializer_class = CartSerializer           #MultiPartParser is used for videos,images for posting.
    # parser_classes = (FormParser,MultiPartParser)  #FormParser is used for images format while posting images
    
class WishlsitViewSet(viewsets.ModelViewSet):
    queryset = WishlistModel.objects.all()
    serializer_class = WishlsitSerializer           #MultiPartParser is used for videos,images for posting.
    # parser_classes = (FormParser,MultiPartParser)  #FormParser is used for images format while posting images
    
