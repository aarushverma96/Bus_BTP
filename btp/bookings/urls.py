from django.conf.urls import url
from bookings import views



urlpatterns = [
	url(r'^jbuses/(?P<gsource>[A-Z][\w-]+)/(?P<gdestination>[A-Z][\w-]+)$', views.jsonallbuses),
	url(r'^jstatus/(?P<gbusId>[0-9][\w-]+)$', views.jsonstatus),
	url(r'buses/(?P<gsource>[A-Z][\w-]+)/(?P<gdestination>[A-Z][\w-]+)$', views.buses),
	url(r'bookings/(?P<gbusId>[0-9][\w-]+)$', views.booking ,name='booking'),
	url(r'search', views.search),
	url(r'customer/(?P<seats>[0-9][\w-]+)$', views.customer, name='customer'),

]