from django import forms
from .models import Gig

class CreateGigForm(forms.ModelForm):
    category = forms.CharField(max_length=150, required=True)
    class Meta:
        model = Gig
        fields = ['name', 'price', 'image','category', 'description']
