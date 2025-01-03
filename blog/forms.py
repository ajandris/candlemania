from django import forms

from .models import BlogPost

class BlogPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Enter title',
            'class': 'w3-input w3-animate-input'
        })
        self.fields['approved'].widget.attrs.update({
            'class': 'w3-check',
            'disabled': True
        })
        self.fields['content'].widget.attrs.update({
            'placeholder': 'Enter text',
        })

    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'approved']
