from django.urls import path
from users import views

urlpatterns = [
    path('users/', views.users),
    path('register/', views.register),
    path('logout/', views.logout_user)
]