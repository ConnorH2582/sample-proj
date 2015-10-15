from django.conf.urls import include, url, patterns
from django.contrib import admin
from contact_manager.views import IndexView,CreateEventView,EventProfileView,CreateContactView,ContactProfileView,ContactSearchView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^new_event/$', CreateEventView.as_view(), name='create_event'),
    url(r'^(?P<nameyear>[a-z0-9-_]{1,200}[-]{1}[0-9]{4})/$', EventProfileView.as_view(), name='event_profile'),
    url(r'^(?P<nameyear>[a-z0-9-_]{1,200}[-]{1}[0-9]{4})/new_contact/$', CreateContactView.as_view(), name='create_contact'),
    url(r'^contact/(?P<endpoint>[a-z]{2,60}[0-9]{4})/$', ContactProfileView.as_view(), name='contact_profile'),
    url(r'^contact/search_results/$', ContactSearchView.as_view(), name='contact_search'),
)
