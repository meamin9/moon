from django.db import models


# Create your models here.
class Text(models.Model):
    author = models.CharField(max_length=32)
    title = models.CharField(max_length=128)
    content = models.TextField()
    ctime = models.DateTimeField()

    def __unicode__(self):
        return self.title
