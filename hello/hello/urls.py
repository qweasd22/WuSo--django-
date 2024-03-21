from django.contrib import admin
from django.urls import path
from django.urls import re_path
from firstapp import views
from firstapp.views import Reg_User, Auth_User

urlpatterns = [
       path('', views.index),
       path('product/<int:product_id>/', views.product),
       path("product/<int:product_id>/add_cart/", views.add_cart),
       path('register/', Reg_User.as_view(), name="register"),
       path('login/', Auth_User.as_view(), name="login"),
       re_path('logout/', views.logout_user),
       re_path('home/', views.home, name='home'),
       path('admin/', admin.site.urls),
       path('close/', views.close, name='close'),
       path("cart/", views.cart, name="cart")
       
      
]
