from django import forms
from .models import Profile
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):

    name = forms.CharField(label='Name', required=False, max_length=255)
    job = forms.CharField(label='Job', required=False, max_length=255)
    image = forms.ImageField(label='Profile', required=False,
                             widget=forms.FileInput(attrs={'data': 'image'}))
    bio = forms.CharField(label='Bio', required=False,
                          widget=forms.Textarea(attrs={'class':
                                                'materialize-textarea'}))
    sn_facebook = forms.URLField(label='Facebook URL', required=False)
    sn_twitter = forms.URLField(label='Twitter URL', required=False)
    sn_google = forms.URLField(label='Google+ URL', required=False)
    sn_youtube = forms.URLField(label='YouTube URL', required=False)
    sn_medium = forms.URLField(label='Medium URL', required=False)
    sn_github = forms.URLField(label='Github URL', required=False)
    sn_linkedin = forms.URLField(label='LinkedIn URL', required=False)

    class Meta:
        model = Profile

        fields = [
            'name',
            'job',
            'image',
            'bio',
            'sn_facebook',
            'sn_twitter',
            'sn_google',
            'sn_youtube',
            'sn_medium',
            'sn_github',
            'sn_linkedin',
        ]


class UserForm(forms.ModelForm):

    username = forms.CharField(label='Username', required=True, max_length=255)
    email = forms.EmailField(label='Email', required=True)

    class Meta:
        model = User

        fields = [
            'username',
            'email',
        ]
