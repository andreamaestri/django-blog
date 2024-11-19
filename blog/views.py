from django.views.generic import ListView
from .models import Post

class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'post_list'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(status=1)
