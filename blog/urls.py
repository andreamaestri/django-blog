# blog/urls.py
from django.urls import path
from .views import HomeView, PostDetailView

app_name = 'blog'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]
