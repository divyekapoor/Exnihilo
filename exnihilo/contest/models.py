from django.db import models
from django.contrib.auth.models import User
from djangoratings.fields import RatingField

class Photo(models.Model):
    
    author = models.ForeignKey(User)
    image = models.ImageField(upload_to="upload/photos/%Y/%m/%d", max_length=1000)
    blurb = models.CharField(max_length=100)
    rating = RatingField(range=5, can_change_vote=True, allow_delete=True)
    createdate = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return "%s stars (%d): %s" % (str(self.rating.score), self.rating.votes, self.blurb)
