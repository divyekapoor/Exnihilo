from django import forms
from models import Photo

class PhotoForm(forms.ModelForm):
    blurb = forms.CharField(label="Description", widget=forms.Textarea())
    class Meta:
        model = Photo
        exclude = ('author',)
        
