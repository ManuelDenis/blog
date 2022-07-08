from django import forms
from blogapp.models import Comments


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}))

    class Meta:
        model = Comments
        fields = ('content', 'author', 'post')

        widgets = {'author': forms.HiddenInput(), 'post': forms.HiddenInput()}

