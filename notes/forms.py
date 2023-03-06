from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Note
from datetime import datetime





class NoteUpdateForm(forms.ModelForm):



    class Meta:
        model = Note

        fields=[
            'title',
            'content',
            'category',
            'execution_date',
            'priority',
        ]
        widgets = {
            'execution_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'title': forms.TextInput(attrs={'placeholder': 'Enter Title'}),
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 8}),
            'category': forms.TextInput(attrs={'placeholder': 'Enter Category'}),

        }



