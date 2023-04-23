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


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control todo-list-input',
            })
        }

    def __init__(self, *args, **kwargs):
        super(EditItemForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['name'].widget.attrs['value'] = self.instance.name
            self.fields['name'].initial = ''
