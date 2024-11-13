from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True) #String, <input type="text" name="title" class="vTextField" maxlength="200" required="" id="id_title">
    slug = models.SlugField(max_length=200, unique=True) #String, <input type="text" name="slug" class="vTextField" maxlength="200" required="" id="id_slug">
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts") #String, <select name="author" data-context="available-source" required="" id="id_author">
    content = models.TextField() #String, <a class="related-widget-wrapper-link change-related" id="change_id_author" data-href-template="/admin/auth/user/__fk__/change/?_to_field=id&amp;_popup=1" data-popup="yes" title="Change selected user">
    created_on = models.DateTimeField(auto_now_add=True) #String
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0) #Int, <select name="status" id="id_status">
    excerpt = models.TextField(blank=True)