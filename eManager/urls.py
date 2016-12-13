from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'emanager'

urlpatterns = [
	url(r'^$', views.EventsListView.as_view(), name='index'),
    url(r'^events/(?P<pk>[0-9]+)/$', views.EventDetailsView.as_view(), name='detail'),
    url(r'^registration/$', views.RegistrationView.as_view(), name='registration'),
    url(r'^login/$', views.LoginView.as_view(), name='login')
]