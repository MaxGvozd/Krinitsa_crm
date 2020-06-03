from django.urls import path
from goods import views

urlpatterns = [
    path('volume/', views.volume),
    path('warehouses/', views.warehouses),
    path('warehouses/create/', views.create_warehouse),
    path('products/create/', views.create_product),
    path('volume/create/', views.create_volume),
    path('products/', views.products),
    path('products/<int:id>', views.retrieve)

]