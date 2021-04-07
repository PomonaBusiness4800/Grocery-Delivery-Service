from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index, name="index_page"),
    path('vons/', views.vons, name="vons"),
    path('vons/search', views.vonsSearch, name="vonsSearch"),
    path('vons/<str:cats>', views.vonsCats, name="vonsCats"),
    path('smart&final/', views.smart_final, name="smart&final"),
    path('smart&final/<str:cats>', views.smartCats, name="smartCats"),
    path('wholefoods/', views.wholefoods, name="wholefoods"),
    path('wholefoods/<str:cats>', views.wholefoodsCats, name="wholefoodsCats"),
    path('traderjoes/', views.traderjoes, name="traderjoes"),
    path('traderjoes/<str:cats>', views.traderjoesCats, name="traderjoesCats"),
    path('food4less/', views.food4less, name="food4less"),
    path('food4less/<str:cats>', views.food4lessCats, name="food4lessCats"),
    path('ralphs/', views.ralphs, name="ralphs"),
    path('ralphs/<str:cats>', views.ralphsCats, name="ralphsCats"),
    path('wholefoods/', views.wholefoods, name="wholefoods"),
    path('register/', views.register, name="register"),
    path('loginPage/', views.loginPage, name="loginPage"),
    path('logout/', views.logoutUser, name="logout"),
    path('userprofile/', views.userprofile, name="userprofile"),
]