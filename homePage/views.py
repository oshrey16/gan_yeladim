from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello. This is our home page! WELCOME!")