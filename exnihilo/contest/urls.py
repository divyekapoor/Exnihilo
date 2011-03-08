from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',

    # Contest url files
    (r'^$', views.index),
    (r'^index.html$', views.index),
)
