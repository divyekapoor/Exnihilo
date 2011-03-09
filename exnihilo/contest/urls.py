from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',

    # Contest url files
    (r'^(?:index.html)?$', views.index),
    (r'^gallery/', views.gallery),
    (r'^submit/', views.submit)
)
