from __future__ import unicode_literals
from django.db import models

class Article(models.Model):

    title = models.Charfield(max_length=255)
    text = model.TextField()
    pub_date = models.DateField()



