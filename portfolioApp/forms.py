from django import forms
from django.core import validators
from portfolioApp.models import UserMessage
from django.forms import ModelForm
class UserData(forms.ModelForm):
    # name=forms.CharField(max_length=264)
    # email=forms.EmailField()
    # message=forms.CharField(widget=forms.Textarea)
    # botcatcher=forms.CharField(required=False,
    #                             widget=forms.HiddenInput,
    #                             validators=[validators.MaxLengthValidator(0)])
    class Meta:
        model=UserMessage
        fields = '__all__'
