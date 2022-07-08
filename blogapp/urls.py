from django.urls import path
from blogapp.views import PostList, PostDetail

urlpatterns = [
    path('', PostList.as_view(), name='index'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
]