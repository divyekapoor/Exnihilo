# Create your views here.
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Q
from djangoratings.views import AddRatingFromModel
import simplejson as json

import models
import forms
import exnihilo.settings as settings

def index_redirect(request):
    # Redirect from site root
    return HttpResponseRedirect(reverse(index))

def index(request):
    # Home Page
    qs = models.Photo.objects.all()
    qs = qs.extra(select={
        'rating_value': '((100/%s*rating_score/(rating_votes+%s))+100)/2' % (models.Photo.rating.range, models.Photo.rating.weight)
    })
    qs = qs.order_by('-rating_value')[:5]
    top5 = qs
    recent = models.Photo.objects.order_by('-createdate')[:5]

    ctx = {'title' : 'Home', 'top5':top5, 'recent':recent}
    return render_to_response('index.html', ctx, context_instance=RequestContext(request))
    
def gallery(request):
    # Gallery page
    my_photo_list = None
    if request.user.is_authenticated():
        my_photo_list = models.Photo.objects.filter(author=request.user)
    
    qs = models.Photo.objects.all()
    qs = qs.extra(select={
        'rating_value': '((100/%s*rating_score/(rating_votes+%s))+100)/2' % (models.Photo.rating.range, models.Photo.rating.weight)
    })
    qs = qs.order_by('-rating_value')
    ctx = {'title':'Gallery', 'photo_list':qs, 'my_photo_list': my_photo_list, 'request' : request }
    return render_to_response('gallery.html', ctx, context_instance=RequestContext(request))
    
def details(request):
    # Contest details page
    ctx = {'title':'Contest Details',}
    return render_to_response('contest_details.html', ctx, context_instance=RequestContext(request))
    
@login_required
def submit(request):
    # Submission to gallery page
    ctx = {'title':'Submit Contest Entry', 'form':None}
    my_photo = models.Photo(author=request.user)
    if request.method == "POST":
        form = forms.PhotoForm(request.POST, request.FILES, instance=my_photo)
        if form.is_valid():
            photo = form.save()
            ctx['form'] = form
            ctx['submission_url'] = settings.SITE_ROOT + reverse(photo_detail, args=[photo.id])
            return render_to_response('submit_done.html', ctx, context_instance=RequestContext(request))
    else:
        form = forms.PhotoForm(instance=my_photo)
    
    ctx['form'] = form
    return render_to_response('submit.html', ctx, context_instance=RequestContext(request))
    


def photo_detail(request, photo_id):
    photo = get_object_or_404(models.Photo, pk=photo_id)
    ctx = {'title':'Photo Details', 'photo':photo, 'request':request, 'submission_url': settings.SITE_ROOT + reverse(photo_detail, args=[photo.id])}
    return render_to_response('comments.html', ctx, context_instance=RequestContext(request))
    
    
def rate(request, object_id, score):
    modelRating = AddRatingFromModel()
    result = modelRating.__call__(request,'photo','contest',object_id,'rating',score)
    message = result.content
    photo = get_object_or_404(models.Photo, pk=object_id)
    rating = photo.rating.get_rating()
    votes = photo.rating.votes
    d = {'id': photo.id, 'rating' : rating, 'votes' : votes, 'message' : message}
    result.content = json.dumps(d)
    return result
