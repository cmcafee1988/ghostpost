from django import forms
from ghostpost_app.models import Post

class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'post_type']