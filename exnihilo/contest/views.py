# Create your views here.
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

def index(request):
    ctx = { 'title' : 'Home'}
    return render_to_response('index.html', ctx, context_instance=RequestContext(request))
