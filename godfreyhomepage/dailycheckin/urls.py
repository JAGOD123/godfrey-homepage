from django.urls import path
from . import views

app_name = 'dailycheckin'

urlpatterns = [
    # The name is what is used for accessing this link from other areas so it would be
    # {{ % url 'users:register' % }}
    path('checkin/', views.check_in, name="checkin"),
]