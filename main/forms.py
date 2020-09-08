from .models import Person
from django.forms import ModelForm, TextInput, Textarea


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['title', 'person']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
                ''
            }),
            "person": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            })
        }
