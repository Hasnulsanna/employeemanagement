from django.urls import path
#from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about1/', views.AboutView.as_view(), name='about1')
]