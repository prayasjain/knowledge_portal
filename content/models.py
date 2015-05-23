from django.db import models

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=300)
    tags = models.TextField(blank=True,null=True)
    date = models.DateTimeField()
    abstract = models.TextField(null=True,blank=True)
    image = models.FileField(null=True,blank=True)
    links = models.TextField(null=True,blank=True)
    content_id = models.AutoField(primary_key=True)

    def __unicode__(self):
        return self.title
