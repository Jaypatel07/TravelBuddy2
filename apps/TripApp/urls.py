from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
    url(r'^destination/(?P<id>\d+)$', views.destination),
    url(r'^add$', views.add),
    url(r'^process_trip$', views.processTrip),
    url(r'^edit/(?P<id>\d+)$', views.edit), 
    url(r'^edit_trip/(?P<id>\d+)$', views.editTrip),
    url(r'^join/(?P<id>\d+)$', views.join),
    url(r'^deletejoin/(?P<id>\d+)$', views.deletejoin),
    url(r'^delete/(?P<id>\d+)$', views.delete),
      
]
