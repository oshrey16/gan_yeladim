from django.http import HttpResponse


def index(request):
    #return HttpResponse("Hello, world. You're at the kidsPage.")
    return render(request,"kidsPage.html")