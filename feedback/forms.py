from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'comment']
        widgets = {'comment': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Deixe seu feedback aqui...'}) }
    