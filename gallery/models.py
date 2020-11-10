from django.db import models

# Create your models here.

class Image(models.Model):
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return " image url: %s" % self.url

class Video(model.Model):
    url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return " video url: %s" % self.url
