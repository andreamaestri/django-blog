from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Post

class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'post_list'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(status=1)

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Post.objects.filter(status=1)

def post_detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug, status=1)
    return render(request, 'post_detail.html', {'post': post})