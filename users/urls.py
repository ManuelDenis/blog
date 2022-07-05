from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import RegisterView, ProfileUpdateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='users-register'),
    path('login/', views.login_page, name='login'),
    path('', LogoutView.as_view(template_name='blogapp/index.html'), name='logout'),
    path('profile/', views.get_profile, name='profile'),
    path('update/<int:pk>/', ProfileUpdateView.as_view(), name='update'),
]
