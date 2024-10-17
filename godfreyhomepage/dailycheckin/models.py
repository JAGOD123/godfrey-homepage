from django.db import models
from django.forms import CharField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class CheckIn(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    journal = models.CharField(max_length=2000)
    teeth = models.PositiveIntegerField(default=2, validators=[MinValueValidator(1), MaxValueValidator(2)])
    sleep = models.PositiveIntegerField()
    skincare = models.PositiveIntegerField()
    gym_hours = models.PositiveIntegerField()
    coding_hours = models.PositiveIntegerField()
    pages_read = models.PositiveIntegerField() #This could be a sperate section with a current reads

    def __str__(self):
        return self.title