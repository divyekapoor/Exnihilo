# Create your views here.
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from forms import PhotoForm

def index(request):
    # Home Page
    ctx = {'title' : 'Home'}
    return render_to_response('index.html', ctx, context_instance=RequestContext(request))
    
def gallery(request):
    # Gallery page
    ctx = {'title' : 'Gallery'}
    return render_to_response('gallery.html', ctx, context_instance=RequestContext(request))
    
# TODO
@login_required
def submit(request):
    # Submission to gallery page
    ctx = {'title':'Submit', 'form':None}
    if request.method == "POST":
        form = PhotoForm(request)
        if form.is_valid():
            photo = form.save()
            ctx['form'] = form
            ctx['submission_url'] = photo.get_url()
            return render_to_response('submit_done.html', ctx, context_instance=RequestContext(request))
    else:
        form = PhotoForm()
    
    ctx['form'] = form
    return render_to_response('submit.html', ctx, context_instance=RequestContext(request))
    
