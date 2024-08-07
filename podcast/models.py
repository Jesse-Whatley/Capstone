from django.db import models

# Create your models here.
class Podcast(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    image = models.ImageField(upload_to='podcasts')
    link = models.URLField()
    
    def __str__(self):
        return F"{self.title} - {self.link}"