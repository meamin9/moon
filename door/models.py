from django.db import models


# Create your models here.
class TimeLog(models.Model):
    ctime = models.DateTimeField()
    mtime = models.DateTimeField()
    atime = models.DateTimeField()


class Role(models.Model):
    name = models.CharField(max_length=32)
    title = models.CharField(max_length=32, blank=True)
    time = TimeLog()
    exp = models.BigIntegerField(default=0)


class Text(models.Model):
    author = models.ForeignKey(Role)
    title = models.CharField(max_length=128)
    content = models.TextField()
    time = TimeLog()

    def __unicode__(self):
        return self.title
