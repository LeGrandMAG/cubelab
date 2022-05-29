from django.urls import path, include
from . import views


urlpatterns = [
    path('register/', views.ProductRegistration, name = 'ProductRegistration' ),
    path('', views.Home, name = 'Home' ),
    path('login/', views.LoginPage, name='login'),
    path('about/', views.About, name="About"),
    path('thankyou/', views.thankyou, name="thankyou")
]