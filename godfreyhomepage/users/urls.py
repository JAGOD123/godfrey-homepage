from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # The name is what is used for accessing this link from other areas so it would be
    # {{ % url 'users:register' % }}
    path('register/', views.register_user, name="register"),
]