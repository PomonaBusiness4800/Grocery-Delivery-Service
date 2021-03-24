from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index, name="index_page"),
    path('vons/', views.vons, name="vons"),
    path('smart&final/', views.smart_final, name="smart&final"),
    path('wholefoods/', views.wholefoods, name="wholefoods"),
    path('traderjoes/', views.traderjoes, name="traderjoes"),
    path('food4less/', views.food4less, name="food4less"),
    path('ralphs/', views.ralphs, name="ralphs"),
    path('wholefoods/', views.wholefoods, name="wholefoods"),
    path('register/', views.register, name="register"),
    path('loginPage/', views.loginPage, name="loginPage"),
    path('logout/', views.logoutUser, name="logout"),
    path('userprofile/', views.userprofile, name="userprofile"),
]