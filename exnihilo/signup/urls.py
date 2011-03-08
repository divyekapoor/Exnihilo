from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',

    # Contest url files
    (r'^$', views.signup),
    (r'^done/$', views.signup_done),
)
