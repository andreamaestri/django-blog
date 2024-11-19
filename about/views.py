from django.views.generic import TemplateView
from .models import Andrea

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['andrea'] = Andrea.objects.first() 
        return context