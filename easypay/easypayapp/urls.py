from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('about', views.about, name='about'),
      path('contact', views.contact, name='contact'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('user_register/', views.user_register, name='user_register')
]
