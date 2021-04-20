from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index, name="index_page"),
    path('vons/', views.vons, name="vons"),
    path('vons/<int:item_id>', views.vonsAddCart, name="vonsAddCart"),
    path('vons/search', views.vonsSearch, name="vonsSearch"),
    path('vons/<str:cats>', views.vonsCats, name="vonsCats"),
    path('smart&final/', views.smart_final, name="smart&final"),
    path('smart&final/<int:item_id>', views.smart_finalAddCart, name="smart&finalAddCart"),
    path('smart&final/search', views.smart_finalSearch, name="smart&finalSearch"),
    path('smart&final/<str:cats>', views.smartCats, name="smartCats"),
    path('wholefoods/', views.wholefoods, name="wholefoods"),
    path('wholefoods/<int:item_id>', views.wholefoodsAddCart, name="wholefoodsAddCart"),
    path('wholefoods/search', views.wholefoodsSearch, name="wholefoodsSearch"),
    path('wholefoods/<str:cats>', views.wholefoodsCats, name="wholefoodsCats"),
    path('traderjoes/', views.traderjoes, name="traderjoes"),
    path('traderjoes/<int:item_id>', views.traderjoesAddCart, name="traderjoesAddCart"),
    path('traderjoes/search', views.traderjoesSearch, name="traderjoesSearch"),
    path('traderjoes/<str:cats>', views.traderjoesCats, name="traderjoesCats"),
    path('food4less/', views.food4less, name="food4less"),
    path('food4less/search', views.food4lessSearch, name="food4lessSearch"),
    path('food4less/<int:item_id>', views.food4lessAddCart, name="food4lessAddCart"),
    path('food4less/<str:cats>', views.food4lessCats, name="food4lessCats"),
    path('ralphs/', views.ralphs, name="ralphs"),
    path('ralphs/<int:item_id>', views.ralphsAddCart, name="ralphsAddCart"),
    path('ralphs/search', views.ralphsSearch, name="ralphsSearch"),
    path('ralphs/<str:cats>', views.ralphsCats, name="ralphsCats"),
    path('wholefoods/', views.wholefoods, name="wholefoods"),
    path('staterbros/', views.staterbros, name="staterbros"),
    path('elsuper', views.elsuper, name="elsuper"),
    path('register/', views.register, name="register"),
    path('loginPage/', views.loginPage, name="loginPage"),
    path('logout/', views.logoutUser, name="logout"),
    path('userprofile/', views.userprofile, name="userprofile"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('payment/<int:address>', views.payment, name="payment"),
    path('confirmation/<int:payment>', views.confirmation, name="confirmation"),
    path('orderconfirmed/<int:order>', views.orderconfirmed, name="orderconfirmed"),
    path('orders/', views.orders, name="orders"),
]