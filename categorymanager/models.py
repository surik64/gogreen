from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    CategoryName = models.CharField(max_length=200, blank=False)
    CatStatus = models.IntegerField(default=1, null=True, blank=True)

class SubCategoryModel(models.Model):
    Category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name="sub")
    SubCategoryName = models.CharField(max_length=200)
    SubCatStatus = models.IntegerField(default=1, null=True, blank=True)


 