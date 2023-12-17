from django.urls import path
from comments import views


urlpatterns = [
    path('likes/', views.LikeList.as_view()),
    path('likes/<int:pk>/', views.CommentDetail.as_view()),
]