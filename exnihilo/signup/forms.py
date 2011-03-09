from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from models import UserProfile

class UserProfileCreationForm(UserCreationForm):
    """
        A form that creates the User Profile with no privileges 
    """
    pic = forms.ImageField(label="Profile Pic")
    about_me = forms.CharField(max_length=1000, widget=forms.Textarea())
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')
    
    def save(self, *args, **kwargs):
        new_user = super(UserProfileCreationForm, self).save(*args, **kwargs)
        UserProfile.objects.create(user=new_user, pic=self.cleaned_data["pic"], about_me=self.cleaned_data["about_me"])
        

class UserProfileModelForm(forms.ModelForm):
    class Meta:
        model = UserProfile
