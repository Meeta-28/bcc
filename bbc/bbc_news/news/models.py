

from django.db import models

class articles(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    date_posted = models.DateTimeField(auto_now_add=True)
