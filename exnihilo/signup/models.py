from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
class UserProfile(models.Model):
    
    user = models.OneToOneField(User)
    pic = models.ImageField(upload_to="uploads", max_length=1000, verbose_name = "Profile Pic")
    about_me = models.CharField(max_length=1000)
    
    def __unicode__(self):
        return u"%s: %s" % (unicode(self.user), self.about_me)
        
        
admin.site.register(UserProfile)
