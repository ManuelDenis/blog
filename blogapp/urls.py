from django.urls import path
from blogapp.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]