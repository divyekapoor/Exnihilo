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
    (r'^$', 'exnihilo.contest.views.index_redirect'),
    
    # Use django.contrib.auth for login management
    (r'^accounts/signup/', include('exnihilo.signup.urls')),
    (r'^accounts/edit/$', 'exnihilo.signup.views.edit_profile'),
    (r'^accounts/edit/password/$', 'exnihilo.signup.views.edit_password'),
    (r'^accounts/profile/(?:([a-zA-Z0-9@\.+\-_]+)/)?$', 'exnihilo.signup.views.profile'),
    (r'^accounts/', include('django.contrib.auth.urls')),
)
