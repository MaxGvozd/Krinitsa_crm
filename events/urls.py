from django.urls import path
from events import views

urlpatterns = [
    path('sale/create/', views.crate_sale),
    path('sale/', views.sale)
]