from django.contrib import admin
from .models import Andrea

# Register your models here.
@admin.register(Andrea)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'job', 'created_on')
