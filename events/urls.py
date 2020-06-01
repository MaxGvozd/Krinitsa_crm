from django.urls import path
from events import views

urlpatterns = [
    path('sale/', views.sale),
]