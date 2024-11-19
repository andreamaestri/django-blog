from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Post

class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'post_list'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(status=1)

class PostDetailView(DetailView):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        """Filter for published posts only"""
        return Post.objects.filter(status=1)

    def get_object(self, queryset=None):
        """Get the specific post object or return 404"""
        if queryset is None:
            queryset = self.get_queryset()
        
        slug = self.kwargs.get(self.slug_url_kwarg)
        return get_object_or_404(queryset, slug=slug)

    def get_context_data(self, **kwargs):
        """Add additional context data"""
        context = super().get_context_data(**kwargs)
        context['coder'] = 'Andrea'
        return context
