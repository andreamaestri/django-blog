
from django import forms
from .models import Collaboration

class CollaborationForm(forms.ModelForm):
    class Meta:
        model = Collaboration
        fields = ['name', 'email', 'project_idea']
        widgets = {
            'project_idea': forms.Textarea(attrs={'rows': 4}),
        }