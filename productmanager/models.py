from django.db import models
from categorymanager.models import SubCategoryModel

# Create your models here.
class ProductModel(models.Model):
    subcategory = models.ForeignKey(SubCategoryModel, on_delete=models.CASCADE)
    Product_Title = models.CharField(max_length=200, blank=False)
    Product_Description = models.TextField()
    Product_Price = models.DecimalField(max_digits=6, decimal_places=2)
    Product_Property = models.CharField(max_length=50, blank=False)
    Product_Cover_Image = models.ImageField(upload_to='products')
    Image1 = models.ImageField(upload_to='products', null=True, blank=True)
    Image2 = models.ImageField(upload_to='products', null=True, blank=True)
    Image3 = models.ImageField(upload_to='products', null=True, blank=True)
    Image4 = models.ImageField(upload_to='products', null=True, blank=True)
    
