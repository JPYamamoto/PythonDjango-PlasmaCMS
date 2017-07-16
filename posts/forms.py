from django import forms
from .models import Post, Comment
from categories.models import Category


class PostForm(forms.ModelForm):
    title = forms.CharField(label='Title', required=True, max_length=150)
    content = forms.CharField(label='Content', required=True,
                              widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))
    category = forms.ModelChoiceField(label='Category', required=True,
                                      queryset=Category.objects.all(),
                                      initial=0,
                                      widget=forms.Select)
    allow_comments = forms.BooleanField(label='Allow Comments', required=False)
    cover_image = forms.ImageField(label='Cover', required=False,
                                   widget=forms.FileInput(attrs={
                                            'data': 'image'}))

    class Meta:
        model = Post

        fields = [
            'title',
            'content',
            'category',
            'allow_comments',
            'cover_image',
        ]


class CommentForm(forms.ModelForm):
    title = forms.CharField(label='Title', required=False, max_length=50)
    content = forms.CharField(label='Content', required=True,
                              widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))

    class Meta:
        model = Comment

        fields = [
            'title',
            'content'
        ]
