from django.http import HttpRequest, HttpResponse

def signup(request):
    return HttpResponse("Signup")
    
def signup_done(request):
    return HttpResponse("Signup Done")
