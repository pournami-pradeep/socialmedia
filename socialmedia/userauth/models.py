from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id_user = models.IntegerField(primary_key=True,default=0)
    bio = models.TextField(blank=True,default='')
    profileimg = models.ImageField(upload_to='profile_images',default='profile.png')
    location = models.CharField(max_length=100,blank=True,default='')

    def __str__(self):
        return self.user.username