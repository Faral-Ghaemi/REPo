from django.urls import path
from . import views

app_name = 'git'
urlpatterns = [
    path('', views.index , name='index'),
    path('myrep/', views.userrepView, name='myrep'),
    path('<str:username>/<str:name>/', views.repview, name='repview')
]
