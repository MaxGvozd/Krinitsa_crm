from django.urls import path
from users import views
from django.urls import path


urlpatterns = [
    path('register/', views.register),
    path('logout/', views.logout_user)
]