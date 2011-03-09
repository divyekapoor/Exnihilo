from django.http import HttpRequest, HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from exnihilo.signup.forms import UserProfileCreationForm, UserProfileModelForm

def signup(request):
    ctx = { 'title' : 'Signup', 'form' : None}
    
    if request.method == "POST":
        form = UserProfileCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(signup_done))
    else:
        form = UserProfileCreationForm()

    ctx['form'] = form
    return render_to_response("signup.html", ctx, context_instance=RequestContext(request))
    
def signup_done(request):
    ctx = {'title' : 'Signup Successful'}
    return render_to_response("signup_done.html", ctx, context_instance=RequestContext(request))

# TODO
def profile(request, user_name):
    """
        Returns a profile page for the logged in User (or other User if username provided)
    """
    ctx = {'title':None,'profile':None}
    if user_name == "":
        if request.user.is_authenticated():
            ctx['profile'] = request.user
        else:
            return HttpResponseNotFound("The user profile that you've requested does not exist.")
    else:
        ctx['profile'] = get_object_or_404(User, username=user_name)

    ctx['title'] = ctx['profile'].get_full_name()
    return render_to_response('profile.html', ctx, context_instance=RequestContext(request))
            
        
# TODO
@login_required    
def edit(request):
    """
        Edit the profile of the currently logged in user
    """
    ctx = {'title' : 'Edit Profile', 'form' : None, 'is_saved' : False}
    if request.method == "POST":
        form = UserProfileModelForm(request.POST, instance=request.user.get_profile())
        ctx["form"] = form
        if form.is_valid():
            form.save()
            ctx["is_saved"] = True
    else:
        form = UserProfileModelForm(instance=request.user.get_profile())
        ctx["form"] = form
        
    return render_to_response('signup.html', ctx, context_instance=RequestContext(request))
    
