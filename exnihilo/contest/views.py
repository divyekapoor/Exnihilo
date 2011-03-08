# Create your views here.
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('index.html', {}, context_instance=RequestContext(request))
