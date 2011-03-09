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
        return new_user
        

class UserProfileModelForm(forms.ModelForm):

    pic = forms.ImageField(label="Profile pic", required=False)
    about_me = forms.CharField(max_length=1000, widget=forms.Textarea(), required=False)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)
        
#    def __init__(self, *args, **kwargs):
#        instance = kwargs.get('instance', None)
#        if instance is None:
#            raise ValueError('This class requires an instance to be provided.')
#        return super(UserProfileModelForm, self).__init__(self, *args, **kwargs)
        
    def save(self, *args, **kwargs):
        new_user = super(UserProfileModelForm, self).save(*args, **kwargs)
        profile = new_user.get_profile()
        if self.cleaned_data["pic"] is not None:
            profile.pic = self.cleaned_data["pic"]
            
        if self.cleaned_data["about_me"] is not None:
            profile.about_me = self.cleaned_data["about_me"]
    
        profile.save()
        return new_user
        

