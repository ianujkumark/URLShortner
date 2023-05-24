from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='creat'),
    path('<str:pk>', views.go, name='go')
]
