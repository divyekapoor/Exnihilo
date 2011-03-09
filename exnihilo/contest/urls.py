from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',

    # Contest url files
    (r'^$', views.index),
    (r'^gallery/', views.gallery),
    (r'^submit/', views.submit),
    (r'^details/', views.details)
    
)
