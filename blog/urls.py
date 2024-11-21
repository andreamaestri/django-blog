from django.urls import path
from .views import HomeView, PostDetailView, AddCommentView, edit_comment, delete_comment

app_name = 'blog'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/add_comment/', AddCommentView.as_view(), name='add_comment'),
    path('post/<int:post_pk>/edit_comment/<int:pk>/', edit_comment, name='edit_comment'),
    path('post/<int:post_pk>/delete_comment/<int:pk>/', delete_comment, name='delete_comment'),
]
