from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name="index")
    path('storeview', views.storeview, name="storeview")
]