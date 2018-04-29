from django.conf.urls import url
from bookings import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
	url(r'^jbuses/(?P<gsource>[A-Z][\w-]+)/(?P<gdestination>[A-Z][\w-]+)$', views.jsonallbuses),
	url(r'^jstatus/(?P<gbusId>[0-9][\w-]+)$', views.jsonstatus),
	url(r'buses/(?P<gsource>[A-Z][\w-]+)/(?P<gdestination>[A-Z][\w-]+)$', views.buses),
	url(r'bookings/(?P<gbusId>[0-9][\w-]+)$', views.booking ,name='booking'),
	url(r'search', views.search),
	url(r'customer/(?P<seats>[0-9][\w-]+)$', views.customer, name='customer'),
	url(r'test/(?P<gbusId>[0-9][\w-]+)$', csrf_exempt(views.test)),
	url(r'mail$', views.mail),
	url(r'delete/(?P<gbusId>[0-9][\w-]+)$',  csrf_exempt(views.delete) ,name='delete'),

]