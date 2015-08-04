from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.

    username = models.TextField(unique=True)
    fullname = models.TextField(max_length=256)
    email = models.EmailField()
    contact = models.BigIntegerField()
    linkedin = models.TextField()
    user_type = models.TextField()
    user_interests = models.TextField()
    education = models.TextField()
    password = models.TextField()
    slug = models.SlugField(unique=True,default='')
    def save(self, *args, **kwargs):
                self.slug = slugify(self.username)
                super(UserProfile, self).save(*args, **kwargs)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.username

