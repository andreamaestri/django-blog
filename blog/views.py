from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from .models import Post
from .forms import CommentForm

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        
        if self.request.user.is_authenticated:
            # Get all comments for authenticated users
            comments = post.comments.order_by("-created_on")
        else:
            # Get only approved comments for anonymous users
            comments = post.comments.filter(approved=True).order_by("-created_on")
            
        comment_count = post.comments.filter(approved=True).count()
        context['comments'] = comments
        context['comment_count'] = comment_count
        return context

class AddCommentView(View):
    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
            return redirect('blog:post_detail', slug=post.slug)
        return redirect('blog:post_detail', slug=post.slug)
