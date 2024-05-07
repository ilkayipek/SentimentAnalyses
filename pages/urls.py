from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.homePage),
    path('verigetir/', views.getSentimentAnlyse, name="verigetir"),
    path('homepage/', views.homePage),
    path('about/', views.about),
    path('cominicate/', views.communicate),
    path('user/', include('userContent.urls')),

]