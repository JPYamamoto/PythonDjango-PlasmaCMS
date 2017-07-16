from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    name = forms.CharField(label='Name', required=True, max_length=150)
    description = forms.CharField(label='Description', required=True)
    icon = forms.ImageField(label='Icon', required=True,
                            widget=forms.FileInput(attrs={'data': 'image'}))
    cover = forms.ImageField(label='Cover', required=True,
                             widget=forms.FileInput(attrs={'data': 'image'}))

    class Meta:
        model = Category

        fields = [
            'name',
            'description',
            'icon',
            'cover',
        ]
