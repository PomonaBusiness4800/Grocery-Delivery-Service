from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name="index"),
    path('storeview/', views.storeview, name="storeview"),
    path('storelist/', views.storelist, name="storelist"),
    path('register/', views.register, name="register"),
    path('loginPage/', views.loginPage, name="loginPage"),
    path('logout/', views.logoutUser, name="logout"),
    path('userprofile/', views.userprofile, name="userprofile"),
    
]