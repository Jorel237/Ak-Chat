from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('signin', views.register, name='signin'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),   
    path('entity', views.entity, name='entity'),
    path('posts/<str:pk>', views.postz, name='post'),   
    path('profile/<str:ak>', views.profile, name='profile'),
    path('getMessage/<str:room>/', views.getMessage, name='getMessage'),
    path('<str:room>/', views.room, name='room'),
    path('check', views.check, name='check'),
    path('send', views.send, name='send'),
       

   

    
]