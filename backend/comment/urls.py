from django.urls import path
from . import views

urlpatterns = [
    # path('all/', views.comment_list), 
    path('', views.user_comments),
    path('all/', views.get_all_comments),
    path('<str:videoId>/', views.get_all_video_comments), 
    # path('video/', views.get_all_video_comments),
]