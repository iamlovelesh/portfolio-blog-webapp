from django import forms
from blog.models import Post,Comment

class PostFrom(forms.ModelForm):# Form for the post

    class Meta():
        model=Post
        fields=('author','title','text')

        widgets={
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }
        help_texts={
            'text':None,
        }


class CommentFrom(forms.ModelForm):

    class Meta():
        model=Comment
        fields=('author','text')

        widgets={
            'author': forms.TextInput(attrs={'class':'textinputclass form-control','placeholder':'Full Name'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
        help_text={
            'text':None,
        }
