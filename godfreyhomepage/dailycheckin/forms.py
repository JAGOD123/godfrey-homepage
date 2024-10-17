from django import forms
from .models import CheckIn

class CheckInForm(forms.ModelForm):
    class Meta:
        model = CheckIn
        fields = ['title', 'journal', 'teeth', 'sleep', 'skincare', 'gym_hours', 'coding_hours', 'pages_read']
        widgets = {
            'journal': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'teeth': forms.NumberInput(attrs={'class': 'form-control'}),
            'sleep': forms.NumberInput(attrs={'class': 'form-control'}),
            'skincare': forms.NumberInput(attrs={'class': 'form-control'}),
            'gym_hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'coding_hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'pages_read': forms.NumberInput(attrs={'class': 'form-control'}),
        }