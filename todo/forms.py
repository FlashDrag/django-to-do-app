from django import forms
from .models import Item


class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control todo-list-input',
                'placeholder': 'What do you need to do today?'
            })
        }
