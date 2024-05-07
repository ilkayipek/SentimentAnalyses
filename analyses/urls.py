from django.urls import path
from . import views


urlpatterns = [
    path('', views.analyses, name='userAnalyses'),
    path('<int:analyseId>/detail/', views.analyseDetail, name="analyseDetail"),
]