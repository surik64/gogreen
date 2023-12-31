"""gogreen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from django.conf import settings            # For image configuarations
from django.conf.urls.static import static  #for image configurations
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from usermanager.views import SigninView
from drf_yasg import openapi

from categorymanager.views import CategoryViewSet, SubCategoryViewSet
from productmanager.views import ProductViewSet
from ordermanager.views import OrderViewSet, CartViewSet,WishlsitViewSet
router = DefaultRouter()





router.register(r'category', CategoryViewSet)
router.register(r'subcategory', SubCategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'cart', CartViewSet)
router.register(r'wishlist', WishlsitViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Shoping CART API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
    #   contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    #path('category', CategoryViewSet)
    path('signin/',SigninView.as_view()  , name='signin'),
    
    path('', include(router.urls))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #from + line of ocde is url root setting
 