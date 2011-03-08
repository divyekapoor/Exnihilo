from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^exnihilo/', include('exnihilo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    # Contest url files
    (r'^contest/', include('exnihilo.contest.urls')),
    
    # Use django.contrib.auth for login management
    (r'^accounts/', include('django.contrib.auth.urls')),
)
