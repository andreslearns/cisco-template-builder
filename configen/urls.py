from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dhcp', views.dhcp, name='dhcp'),
     path('addip', views.addip, name='addip'),

]
