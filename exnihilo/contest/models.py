from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    
    author = models.ForeignKey(User)
    image = models.ImageField(upload_to="upload/photos/%Y/%m/%d", max_length=1000)
    blurb = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.blurb
