from django.conf.urls.defaults import *
import views


urlpatterns = patterns('',

    # Contest url files
    (r'^$', views.index),
    (r'^gallery/details/(\d+)/', views.photo_detail),
    (r'^gallery/', views.gallery),
    (r'^submit/', views.submit),
    (r'^details/', views.details),
    
    # Ratings
    # url(r'^rate/(?P<object_id>\d+)/(?P<score>\d+)/', AddRatingFromModel(), {
    #    'app_label' : 'contest',
    #    'model' : 'photo',
    #    'field_name' : 'rating'
    #}),
    url(r'^rate/(?P<object_id>\d+)/(?P<score>\d+)/', views.rate),
    
    # Comments
    url(r'^comments/', include('django.contrib.comments.urls'))
    
)
