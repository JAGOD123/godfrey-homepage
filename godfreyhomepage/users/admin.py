from django.contrib import admin
from .models import User

# Register your models here.


# THis allows us to see the data of the webpage from the admin area of django
# if we dont register it then we can see it
admin.site.register(User)