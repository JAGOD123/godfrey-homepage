from django import forms
from .models import CheckIn
from datetime import datetime

class CheckInForm(forms.ModelForm):
    '''
    The Form for the Daily Checkins.
    To update you need to edit the model, add the feild to the list and add the widget 
    '''
    class Meta:
        model = CheckIn
        fields = ['datetime', 'title', 'journal', 'teeth', 'sleep', 'skincare', 'gym_hours', 'coding_hours', 'pages_read']
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'journal': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'teeth': forms.NumberInput(attrs={'class': 'form-control'}),
            'sleep': forms.NumberInput(attrs={'class': 'form-control'}),
            'skincare': forms.NumberInput(attrs={'class': 'form-control'}),
            'gym_hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'coding_hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'pages_read': forms.NumberInput(attrs={'class': 'form-control'}),
        }