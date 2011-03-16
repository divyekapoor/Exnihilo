from django import forms
from models import Photo
from django.contrib.comments.forms import CommentDetailsForm

class PhotoForm(forms.ModelForm):
    blurb = forms.CharField(label="Description", widget=forms.Textarea())
    class Meta:
        model = Photo
        exclude = ('author',)

