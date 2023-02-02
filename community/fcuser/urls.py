from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('list/', views.board_list),
    path('post/', views.board_post),
    path('detail/', views.board_detail),
    path('loginsuc/', views.login_suc),
    path('', views.home)
]