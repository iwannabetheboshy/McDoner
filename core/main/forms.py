from django import forms
from django.forms import ModelForm, TextInput, Textarea
from .models import FeedBack


class FeedBackForm(ModelForm):
    class Meta:
        model = FeedBack
        fields = ['name', 'phone', 'question']

        widgets = {
            "name": TextInput(attrs={
                'autocomplete': 'off',
                'class': 'form-control',
                'id': 'form-name',
                'placeholder': 'Имя',
                'required': 'true',
            }),

            "phone": TextInput(attrs={
                'autocomplete': 'off',
                'class': 'form-control tel',
                'id': 'form-tel',
                'type': 'tel',
                'minlength': '6',
                'placeholder': 'Телефон',
                "pattern" : "\+7 \([0-9]{3}\) [0-9]{3}-[0-9]{2}-[0-9]{2}",
                'required': 'true',
            }),
            
            
            "question": Textarea(attrs={
                'autocomplete': 'off',
                'class': 'form-control',
                'id': 'question',
                'style': 'height: 120px;',
                'placeholder': 'Ваш запрос',
                'required': 'false',
            }),
        }
    def __init__(self, *args, **kwargs):
        super(FeedBackForm, self).__init__(*args, **kwargs)
        self.fields['question'].widget.attrs.pop('required')