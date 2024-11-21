from django.contrib import admin
from .models import Andrea, Collaboration

@admin.register(Andrea)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'job', 'created_on')

@admin.register(Collaboration)
class CollaborationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'project_idea', 'created_on')
    search_fields = ['name', 'email', 'project_idea']
    list_filter = ('created_on',)
