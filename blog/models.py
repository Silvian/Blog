from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField('date published', default=timezone.now())
    content = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog)
    author = models.CharField(max_length=250)
    text = models.TextField()
    published_date = models.DateTimeField('date published', default=timezone.now())

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text



