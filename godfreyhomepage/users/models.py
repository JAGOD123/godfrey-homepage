from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=75)
    slug = models.SlugField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name