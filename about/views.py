from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import messages
from .models import Andrea
from .forms import CollaborationForm

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['andrea'] = Andrea.objects.first()
        context['form'] = CollaborationForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CollaborationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for reaching out! I'll get back to you soon.")
            return redirect('about:about')
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)