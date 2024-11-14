from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True) #String, <input type="text" name="title" class="vTextField" maxlength="200" required="" id="id_title">
    slug = models.SlugField(max_length=200, unique=True) #String, <input type="text" name="slug" class="vTextField" maxlength="200" required="" id="id_slug">
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts") #String, <select name="author" data-context="available-source" required="" id="id_author">
    content = HTMLField()
    created_on = models.DateTimeField(auto_now_add=True) #String
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0) #Int, <select name="status" id="id_status">
    excerpt = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    class Meta:
        ordering = ['-created_on']

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = HTMLField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        body_excerpt = self.body[:100] + '...' if len(self.body) > 100 else self.body
        return f"Comment by {self.author}: {body_excerpt}"

    class Meta:
        ordering = ['created_on']
