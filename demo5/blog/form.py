from django import forms
from comment.models import Comment

class CommentForms(forms.ModelForm):
    class Meta():
        model=Comment
        fields=['name','email','url','content']
        widget={'content':forms.Textarea}