from django import forms
from .models import TextSearch

class TextForm(forms.ModelForm):
    class Meta:
        model = TextSearch
        fields = '__all__'