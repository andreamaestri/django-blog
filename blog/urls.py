from django.urls import path
from .views import HomeView, PostDetailView, AddCommentView

app_name = 'blog'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/add_comment/', AddCommentView.as_view(), name='add_comment'),
]
