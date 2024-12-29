from django.db import models
from django.forms import CharField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify



# Create your models here.
class CheckIn(models.Model):
    #TODO DEBUG: CHANGE THIS BACK ONCE THEY SHOULDNT NEED TO INPUT THE DATE
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=False)
    journal = models.CharField(max_length=2000)
    teeth = models.PositiveIntegerField(default=2, validators=[MinValueValidator(1), MaxValueValidator(2)])
    sleep = models.PositiveIntegerField()
    skincare = models.PositiveIntegerField()
    gym_hours = models.PositiveIntegerField()
    coding_hours = models.PositiveIntegerField()
    #TODO: This could be a sperate section with a current reads linking to the book in Q
    pages_read = models.PositiveIntegerField() 


    def __str__(self):
        return self.title
    
    @property
    def date_slug(self):
        return self.datetime.strftime('%Y-%m-%d')  # Generates the slug in the 'YYYY-MM-DD' format
