from django import forms
from django.contrib.auth.models import User
from .models import Blog


class BlogSettingsForm(forms.ModelForm):

    name = forms.CharField(label='Name', required=True, max_length=150)
    slogan = forms.CharField(label='Slogan', required=False, max_length=200)
    icon = forms.ImageField(label='Logo', required=False,
                            widget=forms.FileInput(attrs={
                                    'data': 'image'}))
    cover = forms.ImageField(label='Cover', required=False,
                             widget=forms.FileInput(attrs={
                                    'data': 'image'}))
    sn_facebook = forms.URLField(label='Facebook URL', required=False)
    sn_twitter = forms.URLField(label='Twitter URL', required=False)
    sn_medium = forms.URLField(label='Medium URL', required=False)
    sn_github = forms.URLField(label='GitHub URL', required=False)
    sn_linkedin = forms.URLField(label='LinkedIn URL', required=False)
    sn_youtube = forms.URLField(label='YouTube URL', required=False)
    sn_google = forms.URLField(label='Google+ URL', required=False)

    class Meta:
        model = Blog

        fields = [
            'name',
            'slogan',
            'icon',
            'cover',
            'sn_facebook',
            'sn_twitter',
            'sn_medium',
            'sn_github',
            'sn_linkedin',
            'sn_youtube',
            'sn_google'
        ]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=20, label='Username')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(),
                                error_messages={'required': 'Required field.',
                                                'unique': 'Username already used.',
                                                'invalid': 'Not valid username.'})
    password2 = forms.CharField(label='Retype password', widget=forms.PasswordInput(),
                                error_messages={'required': 'Required field.'})
    email = forms.EmailField(error_messages={'required': 'Required field.',
                                             'invalid': 'Invalid email.'})

    def clean(self):
        clean_data = super(RegisterForm, self).clean()
        password1 = clean_data.get('password1')
        password2 = clean_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Passwords are different.')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(
                username=username).exists():
            raise forms.ValidationError('Email already used.')
        return email

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')
