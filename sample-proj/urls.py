from django.conf.urls import include, url,patterns
from django.contrib import admin
from django.views.generic import View
from contact_manager.views import IndexView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact_manager/', include('contact_manager.urls', namespace = 'contact_manager', app_name='contact_manager')),
)
