from django.contrib import admin
from .models import Post, Comment
from tinymce import models as tinymce_models

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):  # Change this line
    list_display = ('title', 'slug', 'author', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Comment)
