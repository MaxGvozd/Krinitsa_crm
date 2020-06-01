from django.urls import path
from goods import views

urlpatterns = [
    #path('goods/', views.goods),
    path('create/product/', views.create_product),
    path('create/volume/', views.create_volume),
    path('create/warehouse/', views.create_warehouse),
]