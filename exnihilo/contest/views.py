# Create your views here.
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

import models
import forms

def index(request):
    # Home Page
    ctx = {'title' : 'Home'}
    return render_to_response('index.html', ctx, context_instance=RequestContext(request))
    
def gallery(request):
    # Gallery page
    ctx = {'title':'Gallery', 'photo_list':models.Photo.objects.all() }
    return render_to_response('gallery.html', ctx, context_instance=RequestContext(request))
    
def details(request):
    # Contest details page
    ctx = {'title':'Contest Details'}
    return render_to_response('contest_details.html', ctx, context_instance=RequestContext(request))
    
# TODO
@login_required
def submit(request):
    # Submission to gallery page
    ctx = {'title':'Submit Contest Entry', 'form':None}
    my_photo = models.Photo(author=request.user)
    if request.method == "POST":
        form = forms.PhotoForm(request.POST, request.FILES, instance=my_photo)
        print form
        print form.is_valid()
        if form.is_valid():
            photo = form.save()
            ctx['form'] = form
            ctx['submission_url'] = photo.image.url
            return render_to_response('submit_done.html', ctx, context_instance=RequestContext(request))
    else:
        form = models.PhotoForm(instance=my_photo)
    
    ctx['form'] = form
    return render_to_response('submit.html', ctx, context_instance=RequestContext(request))
    
