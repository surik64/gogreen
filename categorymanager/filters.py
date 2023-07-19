from .models import CategoryModel, SubCategoryModel
from django_filters import rest_framework as filters



class CategoryFilter(filters.FilterSet):

    # def mydef(self, query, obj ):        
    #     return CategoryModel.objects.all()

    # duration = filters.CharFilter(method=mydef)
    class Meta:
        model =CategoryModel
        fields =['CategoryName' ]


    
