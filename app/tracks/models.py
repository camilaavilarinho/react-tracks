from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
## create a database model where we can store and display tracks from our users(that our users create)
## Django is going to turn this model into an individual database table for us

class Track(models.Model):
    # An id field is created automatically and will serve as our primary key for the track
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    # allow us to specify a many to one relationship
    ## -> for may tracks that are created they can only point to one user
    posted_by = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)

# Create Like model to create model table
class Like(models.Model):
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    # tracks.Track give us access to the tracks model
    #related_name allow us to get information of the likes that were being put on a track when we query it.
    track = models.ForeignKey('tracks.Track', related_name='likes', on_delete=models.CASCADE)