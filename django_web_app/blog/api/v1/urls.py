from rest_framework.urls import path
from .view import PosttListCreateAPIView, PostRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('posts/', PosttListCreateAPIView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-detail'),
]