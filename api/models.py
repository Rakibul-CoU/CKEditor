from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.


class YourModel(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()


class Book(models.Model):
    title = models.CharField(max_length=200)
    detail = models.CharField(max_length=200)

    def __str__(self):
        return self.title