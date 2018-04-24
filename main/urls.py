from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('new/', views.BasicRedirView, name='newUrl'),
    path('<id>', views.BasicRedirView, name='redir'),
    path('c/', views.CoinRedirView, name='newCRedir'),
    path('c/<id>', views.CoinRedirView, name='cRedir'),
]