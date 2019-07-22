from django.urls import path
from . import views

app_name = 'git'
urlpatterns = [
    path('', views.index , name='index'),
    path('myrep/', views.userrepView, name='myrep'),
    path('myrep/<int:id>/', views.repview, name='repview'),
    path('createrep/', views.RepCreate, name='repcreate'),
]
