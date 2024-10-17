from django.urls import path
from . import views

app_name = 'dailycheckin'

urlpatterns = [
    # The name is what is used for accessing this link from other areas so it would be
    # {{ % url 'users:register' % }}
    path('checkin/', views.check_in, name="checkin"),
    path('list/', views.checkin_list, name="checkin_list"),
    path('<slug:date_slug>/', views.checkin_details, name="checkin_detail"),

]