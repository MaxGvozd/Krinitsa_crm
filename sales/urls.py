from django.urls import path
from sales import views

urlpatterns = [
    path('create/', views.create_area),
]