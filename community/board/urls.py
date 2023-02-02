from django.urls import path
from . import views

urlpatterns = [

    path('list/', views.board_list),
    path('post/', views.board_post),
    path('detail/<int:pk>/', views.board_detail)
    
    
]