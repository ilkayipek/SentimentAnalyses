from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.getUser),
    path('userdetail/', views.userDetail, name='userDetail'),
    path('userdetail/edit', views.userDetailEdit),
    path('sentimentanalyses/', include('analyses.urls')),
]